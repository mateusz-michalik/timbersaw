#!/usr/bin/env python3

# imports
import os
import glob
import argparse
from subprocess import call

# init
def init():
    print("---------------------------------------------------")
    print("I cut things. It's what I do. What else would I do?")
    print("---------------------------------------------------")

    # params
    parser = argparse.ArgumentParser(description='Timbersaw')
    parser.add_argument('-s', '--source', help='Source folder to search for ranged FLACs', required=True)
    parser.add_argument('-c', '--cleanup', help='Default false, if true will remove source range FLACs')
    args = parser.parse_args()

    # dirs and files
    flac_dir = glob.escape(args.source + '/')
    flacs = glob.glob(flac_dir + '**/*.flac')

    for flac in flacs:
        print(flac)
        flac_dir = os.path.dirname(flac) + "/"
        flac_name = os.path.basename(flac)
        flac_name_without_ext = os.path.splitext(flac_name)[0]
        cue_name = flac_name_without_ext + ".cue"
        cue = flac_dir + cue_name

        print("Attempting to split FLAC: " + flac_name)
        print("Searching for CUE file: " + cue_name + "...")

        if os.path.isfile(cue)==True:
            print("CUE file found, cutting...")
            split = ['shnsplit', '-o', "flac", '-t', "%n - %t", '-f', cue, flac]
            call(split, cwd=flac_dir)

            pre_gap_check = flac_dir + "00 - pregap.flac"
            if os.path.isfile(pre_gap_check)==True:
                print("Removing any pregap into track incorrectly made from CUE...")
                os.remove(pre_gap_check)

            print("Moving tag data from CUE...")
            call("cd " + "'" + flac_dir + "'; cuetag *.cue [0-9]*.flac", shell=True)

            if args.cleanup=="true":
                print("Removing original ranged FLAC...")
                os.remove(flac)

            print("FLAC and CUE cut complete!")
        else:
            print("CUE file not found, moving on...")

        print("---------------------------")

# main script
if __name__ == "__main__":
    init()
