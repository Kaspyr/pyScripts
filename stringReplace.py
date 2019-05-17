#!/usr/bin/python3

from datetime import datetime
import re, sys

if len(sys.argv) != 4:
    exit("\tUSAGE: ./wordReplace <FILE> <ORIGINAL STRING> <NEW STRING>")

def newFileName():
    dt = datetime.now()
    fName = f"{dt.strftime('%H:%M:%S-%m%d%Y')}.log"
    return fName

def fileAppending(line, nFName):
    with open(nFName, 'a+') as f:
        f.write(line)

def stringSearch(filename, oldWord, newWord, nFName):
    with open(filename, 'r+') as orgFile:
        print("\t----- Making File Changes -----")
        listOfLines = orgFile.readlines()
        for line in listOfLines:
            if oldWord not in line:
                #line = line.replace(oldWord, newWord)
                fileAppending(line, nFName)
            else:
                line = re.sub(oldWord, newWord, line)
                print(line)
                fileAppending(line, nFName)

if __name__ == '__main__':
    nFName = newFileName()
    stringSearch(sys.argv[1], sys.argv[2], sys.argv[3], nFName)
    print(f"\t----- New File Called {nFName} -----")

