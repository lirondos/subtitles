import re
import os, os.path

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
    text = unicode(text, 'utf8')
    cleantext = text.encode('utf8', 'replace')
    return cleantext

# rootdir should contain the path to the folder where subtitles files are located 
rootdir = 'C:\\Users\\myuser\\Documents\\subtitles'
for root, _, files in os.walk(rootdir):
    for file in files:
        basename=os.path.basename(file)
        localpath = os.path.realpath(os.path.join(root,basename))
        shakes  = open(localpath, 'r')
        text= shakes.read()
        cleantext=clean(text)
        filename=os.path.splitext(os.path.basename(file))[0]
        # save_path should contain the path to the folder where txt files will be saved
        save_path = 'C:\\Users\\myuser\\Documents\\txt'
        completeName = os.path.join(save_path, filename+'.txt')  
        newfile = open(completeName,'w')
        newfile.write(cleantext)
        newfile.close()
        shakes.close()