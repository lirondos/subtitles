#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import os
import sys
import codecs
from fnmatch import fnmatch

from utils import guess_encoding

import logging
log = logging.getLogger(__file__)


def clean(text):
    #we remove time stamp and scene number
    text=re.sub('\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', text)
    #we remove HTML tags
    text=re.sub('</?.+?>', '', text)
    #we remove subtitle tags (location within the screen, etc)
    text=re.sub('{.+?}', '', text)
    #we remove action description displayed with []
    text=re.sub('\[.+?\]', '', text)
    #we remove lines only containing hyphens (caused by the [] removal)
    text=re.sub('\n-\n', '', text)
    # we remove empty lines
    text=re.sub('\n+', '\n', text)
    # we remove the space at the beginning of a new line (caused by the [] removal)
    text=re.sub('\n ', '\n', text)
    #we encode it as UTF-8
    #text = unicode(text, 'utf8')
    #cleantext = text.encode('utf8', 'replace')
    return text


def process_file(filename, output_filename):
    log.info("Process file '{}'".format(filename))
    try:
        encoding = guess_encoding(filename)
        with codecs.open(filename, 'r', encoding=encoding) as fi:
            # Always write to UTF8 file
            with codecs.open(output_filename, 'w', encoding='utf8') as fd:
                for line in fi:
                    cleaned_text = clean(line)
                    if len(cleaned_text.strip()):
                        fd.write(cleaned_text)
        log.info("\t- output: {}".format(output_filename))
        return True
    except Exception as e:
        log.exception("Unhandled exception")
        return False


def process(rootdir, save_path, flatten, pattern='*.srt'):
    total = success = 0
    for root, _, files in os.walk(rootdir):
        rel_path = os.path.relpath(root, rootdir)
        srt_files = [file for file in files if fnmatch(file, pattern)]
        if srt_files:
            output_path = os.path.join(save_path, rel_path) if not flatten else save_path
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            for file in srt_files:
                filename = os.path.splitext(file)[0]
                output_filename = os.path.join(output_path, filename + ".txt")
                r = process_file(os.path.join(root, file), output_filename)
                if r: success += 1
        total += len(srt_files)
        pass
    return success, total


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Process subtitles files removing metadata.')
    parser.add_argument('-i', '--input-root', dest='input_root', required=True,
                        help='Path to folder (or file) to process where ".srt" files are located')
    parser.add_argument('-o', '--output-path', dest='output_path', required=True,
                        help='Path to folder where files will be saved')
    parser.add_argument('--keep-hierarchy', dest='keep_hierarchy', action='store_true',
                        help='Whether input folder hierarchy will be preserved or flattened (default).')
    parser.add_argument('-d', '--debug', action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING,
                        help="Print lots of debugging statements")
    parser.add_argument('-v', '--verbose', action="store_const", dest="loglevel",
                        const=logging.INFO, help="Be verbose")
    args = parser.parse_args()

    # Configure logging
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root = logging.getLogger('')
    root.addHandler(ch)
    root.setLevel(level=args.loglevel)

    # Sanitize input arguments
    input_root = args.input_root
    if not os.path.exists(input_root):
        sys.stderr.write("Input root '{}' not found or cannot be opened".format(input_root))
        exit(-1)

    # Check output path (create it if not exists)
    output_path = args.output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Work with file or folder
    if os.path.isfile(input_root):
        input_filename = os.path.basename(input_root)
        output_filename = os.path.join(output_path, os.path.splitext(input_filename)[0] + '.txt')
        ret = process_file(input_root, output_filename)
        success = 1 if ret else 0
        total = 1
    else:
        success, total = process(input_root, output_path, flatten=not args.keep_hierarchy)

    errors = total - success
    sys.stdout.write("Processed {:d} files{}.\n".format(total, " ({} with errors)".format(errors) if errors else ""))
