#
# Example for working with OS Path
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the os
    print(os.name)
    # Check if the item exists and type
    print("Item exists: " + str(path.exists("mario.txt")))
    print("Item is a file: " + str(path.isfile("mario.txt")))
    print("Item is a directory: " + str(path.isdir( "mario.txt")))
    print("Item PATH: " + str(path.realpath("mario.txt")))
    print("Item PATH and Name: " + str(path.split(path.realpath("mario.txt"))))

    t = time.ctime(path.getmtime("mario.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("mario.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("mario.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("OR " + str(td.total_seconds()) + "seconds")

if __name__ == "__main__":
    main()