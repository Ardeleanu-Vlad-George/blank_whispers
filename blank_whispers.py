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

xtra_jumps = 0

for char_idx in range(len(code)):
    if xtra_jumps:
        xtra_jumps-=1
        continue
    if code[char_idx] in " \t\n":
        continue
    print(code[char_idx], end='')

    # the 'xtra_jumps' variable will be used to jump over 
    # chars that don't need to further be analyzed
    # this is useful for languages where in order 
    # to start a 'one-line' comment you need a sequence
    # of multiple chars
    if code[char_idx] == 'm':
        xtra_jumps = 2

print()
