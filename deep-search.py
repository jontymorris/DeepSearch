#!/usr/bin/python3

import os
import sys


def get_file_contents(path):
    handle = open(path, 'r')
    contents = handle.read()
    handle.close()

    return contents

def scan_file(file, keywords):
    '''
    Scans a files contents to see if it contains all of the
    keywords. If so, the path will be printed.
    '''

    try:
        contents = get_file_contents(file)

        for keyword in keywords:
            if keyword not in contents:
                return
        
        print('[FOUND] ' + file)
    except:
        print('[ERROR] ' + file)

def scan_folder(path, keywords):
    '''
    Loops through all files in folder. If another folder is found,
    then it will be searched recursively. All files found will be
    scanned for the keywords.
    '''

    for name in os.listdir(path):
        file = os.path.join(path, name)

        if os.path.isdir(file):
            scan_folder(os.path.join(file), keywords)
        else:
            scan_file(file, keywords)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('[usage]')
        print('deep-search (path) (keyword) (keyword)...')
        exit(0)

    scan_folder(sys.argv[1], sys.argv[2:])
