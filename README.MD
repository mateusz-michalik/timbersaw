# Timbersaw
A python script to slice range ripped FLAC files into separate tracks using cue and retaining tag data

## Instructions
Install everything as follows

1. Clone or download timbersaw.py
2. Set permissions using `chmod +x timbersaw.py`
3. Install requirements, for example `brew install cuetools flac ffmpeg shntool`
4. Install `cuetag` for your system (see requirements)

## Requirements
You will need the following installed:

1. `cuetools` and `cuetag` specifically from https://github.com/svend/cuetools/blob/master/src/tools/cuetag.sh or from https://github.com/gumayunov/split-cue/blob/master/cuetag for OSX version of `cuetag.sh`

2. `shntool` which will give you the `shnsplit` command that this Python script Requirements

3. `ffmpeg` and `flac` are handy to have too if you do a lot of commandline transcoding and flac work

## Notes
This was built to split lots of nested folders of range ripped FLAC albums, it could use some work to make it more agnostic, but for now it fulfills its intended purpose.

Beware the script will remove original range ripped FLAC file too, original CUE file will be left intact however.
