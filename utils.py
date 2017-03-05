#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chardet.universaldetector import UniversalDetector

import logging
log = logging.getLogger(__file__)

detector = UniversalDetector()


def guess_encoding(filename):
    # Let's guess encoding for each file (a bit slow, but safer)
    detector.reset()
    with open(filename, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done: break
    detector.close()
    ret = detector.result
    log.debug("\t- encoding: {} ({} confidence)".format(ret['encoding'], ret['confidence']))
    return ret['encoding']


