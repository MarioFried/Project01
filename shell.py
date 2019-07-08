#
# Uso do Shell
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("mario.txt"):
        src = path.realpath("mario.txt")
        print (src)
        dst = src + ".bak"
        # shutil.copy(src,dst)
        # shutil.copystat(src,dst)

        # Renomear
        # os.rename("NewMario.txt","mario.txt")

        # Archive ZIP
        # root_dir, tail = path.split(src)
        # print (root_dir)
        # print (tail)
        # shutil.make_archive("archive","zip",root_dir)

        with ZipFile("TestZip.zip", "w") as newzip:
            newzip.write("mario.txt")
            newzip.write("mario.txt.bak")

if __name__ == "__main__" :
    main()