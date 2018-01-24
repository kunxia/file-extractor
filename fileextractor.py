import shutil
import os
import datetime
import time
import argparse
import ftplib

class FileExtractor:
    def __init__(self):
        print("File Extractor")

    def parse_args(self):
        parser=argparse.ArgumentParser(description='Recursively extract files (optionally with specified file extension) from source to destination')
        parser.add_argument('-s','--src', help='Required: full path to the source folder', dest="source", required=True)
        parser.add_argument('-d','--dest', help='Required: full path to the destination folder. If it does not exist, it will be created.', dest="destination", required=True)
        parser.add_argument('-e','--ext', help='optional: file extension (e.g. .csv), if not specified, all files will be copied over.', dest="extension", required=False)
        return parser.parse_args()

    def search_copy_files(self,source, destination, extension):
        print("Searching and copying files from Source: "+source+" to Destination: "+destination)
        if not os.path.exists(destination):
            os.makedirs(destination)
        for root, directories, filenames in os.walk(source):
            for filename in filenames:
                if extension != None:
                    if filename.endswith(extension):
                        self.__copy_file(root,filename,destination)
                else:
                    self.__copy_file(root,filename,destination)
        print("Finished copying all files. Please check the destination folder:"+destination)

    def __copy_file(self,root, filename, destination):
        try:
            shutil.copy(os.path.join(root,filename),destination)
        except Exception as e:
            print(e)
            pass
        finally:
            print("copied "+os.path.join(destination,filename))

#__main__
if __name__ == '__main__':
    fe=FileExtractor()
    args=fe.parse_args()
    fe.search_copy_files(args.source,args.destination,args.extension)

