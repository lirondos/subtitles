# subtitles
The subtitles repository contains: 
- A Python script that converts a subtitle file (.srt, etc) into a txt file, keeping the actual subtitle and removing:
* time stamp 00:00:06,217 --> 00:00:07,635
* subtitle tags {\an8}
* HTML tags <i>
* scene number 3421
* descriptive noise subtitles [breathing intensifies] 
Given the path to a folder containing subtitle files, creates a new folder where the txt "clean" txt files will be saved.

- A folder with Spanish subtitle clean files in txt from LOTR, Star Wars, Narcos, OITNB, GoT and HIMYM.
This .txt files can be used as corpus material and are ready to be uploaded to AntConc.
