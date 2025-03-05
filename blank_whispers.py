#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Please give just one CLA, otherwise the program can't work")
    exit(-1)

code = ''

with open(sys.argv[1], 'r') as src:
    src = src.readlines()
    for line in src:
        code += line


print(code, end='')
