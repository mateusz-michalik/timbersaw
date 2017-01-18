# Timbersaw
A python script to slice range ripped FLAC files into separate tracks using cue and retaining tag data

## Requirements
You will need the following installed:

1. `cuetools` and `cuetag` specifically from https://github.com/svend/cuetools/blob/master/src/tools/cuetag.sh or from https://github.com/gumayunov/split-cue/blob/master/cuetag for OSX version of `cuetag.sh`

2. `shntool` which will give you the `shnsplit` command that this Python script Requirements

3. `ffmpeg` and `flac` are handy to have too if you do a lot of commandline transcoding and flac work

## Install
Install everything as follows

1. Clone or download timbersaw.py
2. Install requirements, for example `brew install cuetools flac ffmpeg shntool`
3. Install `cuetag` for your system (see requirements)
4. Set permissions using `chmod +x timbersaw.py`

## Instructions
Once everything is installed use the following command. Remember to specifiy the absolute path of the folder you want Timbersaw to look for and split FLACs in.

1. Run timbersaw using `timbersaw.py -s /media/range_flac_albums`
2. Optional param `-c true` will enable cleanup which removes the source ranged FLAC once split is complete

## Notes
This was built to split lots of nested folders of range ripped FLAC albums, it could use some work to make it more agnostic, but for now it fulfills its intended purpose.

Beware the script will remove original range ripped FLAC file too, original CUE file will be left intact however.
