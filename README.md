# subtitles
The subtitles repository contains a folder with Spanish subtitle clean files in txt from LOTR, Star Wars, Narcos, OITNB, GoT and HIMYM (this .txt files can be used as corpus material and are ready to be uploaded to AntConc) and a Python script that converts a subtitle file (.srt, etc) into a txt file, keeping the actual subtitle and removing:

1. time stamp 00:00:06,217 --> 00:00:07,633

2. subtitle tags {\an8}

3. HTML tags 

4. scene number 3421

5. descriptive noise subtitles [breathing intensifies] 


