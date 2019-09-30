# subtitles
This repository contains a corpus of Spanish subtitles of popular films and series. The `txt` folder contains the subtitles txt files from:
- Lord of the Rings
- Star Wars
- Narcos
- Orange Is The New Black
- Game of Thrones 
- How I Met Your Mother. 

The Python script `subtitles.py` can be used to convert any subtitle file (.srt, etc) into a txt file, keeping the actual subtitle text and removing:

1. time stamp 00:00:06,217 --> 00:00:07,633

2. subtitle tags {\an8}

3. HTML tags 

4. scene number 3421

5. descriptive noise subtitles [breathing intensifies] 

This corpus was created for a workshop for high school students from Spain. The workshop consisted of analyzing these subtitles using [AntConc toolkit](https://www.laurenceanthony.net/software/antconc/) as a way of introducing them to Corpus Linguistics. [The making-of of the corpus compilation and the activities done during the workshop can be found here (in Spanish)](http://grammarpunki.com/star-wars-en-clase-de-lengua-los-subtitulos-como-corpus-linguistico/)


