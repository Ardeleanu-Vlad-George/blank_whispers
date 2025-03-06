#!/usr/bin/python3
'''
    In this part we define the constants the program needs in order to work
'''
def Python_comment_detection(idx, src):
    if src[idx] == '#' and src[idx+1] != '!':
        return 2
    return 0

Python_rules = ('Python script', 'py', Python_comment_detection)

def C_comment_detection(idx, src):
    if src[idx] == '/' and src[idx+1] == '/':
        return 2
    return 0

C_rules      = ('C source file', 'c', C_comment_detection)

# Define more rules here, then add them to 'all_rules'

all_rules = (Python_rules, C_rules)


'''
    Entering the 'main' body of the program
'''
import sys

if len(sys.argv) != 2:
    print("Please give just one CLA, otherwise the program can't work")
    exit(-1)

extn_idx = 0

for extn_idx in range(len(sys.argv[1])):
    if sys.argv[1][extn_idx] == '.':
        break

extn = sys.argv[1][extn_idx+1:]

func = None
name = None

for rule in all_rules:
    if extn in rule[1:-1]:
        name = rule[0]
        func = rule[-1]

if func is None:
    print(extn, "is an unknown file extension. Cannot detect it's type for processing.")
    exit(-1)

print("Detected next file type:", name)

code = ''

with open(sys.argv[1], 'r') as file:
    file = file.readlines()
    for line in file:
        code += line

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
    xtra_jumps=func(char_idx, code)
    if xtra_jumps:
        print("Comment detected at: (%d, %d)" % (line_idx, colm_idx))

print("Program ended")
