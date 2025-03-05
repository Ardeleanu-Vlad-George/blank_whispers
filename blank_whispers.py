#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Please give just one CLA, otherwise the program can't work")
    exit(-1)

code = ''

with open(sys.argv[1], 'r') as file:
    file = file.readlines()
    for line in file:
        code += line

def comment_at_in(idx, src):
    if src[idx] == 'm':
        return 2
    return 0

xtra_jumps = 0
line_idx = 1
colm_idx = 0

for char_idx in range(len(code)):
    colm_idx+=1
    if xtra_jumps:
        xtra_jumps-=1
        continue
    if code[char_idx] in " \t\n":
        if code[char_idx] == '\n':
            line_idx+=1
            colm_idx=0
        continue
    # print(code[char_idx], end='')

    # the 'xtra_jumps' variable will be used to jump over 
    # chars that don't need to further be analyzed
    # this is useful for languages where in order 
    # to start a 'one-line' comment you need a sequence
    # of multiple chars
    xtra_jumps = comment_at_in(char_idx, code)
    if xtra_jumps:
        print("Comment detected at: (%d, %d)" % (line_idx, colm_idx))

print("Program ended")
