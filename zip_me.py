"""This is a python script to zip files.
It accepts the file path as a command line argument.
"""
from zipfile import ZipFile
from sys import argv
import os


def get_paths(directory):
    
    """Function to get the path,
    of all the files to be zipped"""

    paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)

    return paths


def main():
    directory = argv[1]

    file_paths = get_paths(directory)
    print("Following files will be zipped: ")
    for filename in file_paths:
        print(filename)

    with ZipFile('my_files.zip', 'w') as zip:
        for file in file_paths:
            zip.write(file)

    print("All files successfully zipped")

if __name__ == "__main__":
    main()