

# Written By Elliott V Iannello
# Made Freely Available to use and edit by others as they see Fit
# 6 - 19 - 2015


import os
import subprocess
import argparse


def iterate_and_apply_to_dir(file_path: str):
    """Loops over files in sub dir and runs the given python program on each file found in respective dirs"""
    fileNumber = 1

    # Be sure to enter Path as String

    rootDirectory = input('Enter Directory Path: ')
    print('Files in:', rootDirectory)

    for subDirectory, dirs, files in os.walk(rootDirectory):
        for file in files:
            print(str(fileNumber) + ": " + os.path.join(subDirectory, file))

            # Change script2.py to desired script to be run on all files and follow with arguments as strings
            subprocess.call(f"python {file_path}" + " " + os.path.join(subDirectory, file) , shell=True)
            fileNumber = fileNumber + 1


# Main
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Operation Iterator .Py')

    parser.add_argument('-f', '--filepath', help="Path to file that is to be executed upon each other file in directory.", default="", dest="file_path")
    args = parser.parse_args()

    if args.file_path == "":
        print("Must provide a File Path for the Python File to be run on each file in Sub Dirs.")
        exit(1)
    else:
        print(f"Running {args.file_path} on each file I can find ... ")
        iterate_and_apply_to_dir(file_path=args.file_path)

