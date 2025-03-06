#!/usr/bin/python3
'''
    In this part we define the constants the program needs in order to work
    These constants will be 'rules' as in 'tuples' each defined for a language
    The first component of the rule is the 'name' of the file type
    The second component is the 'sequence' that activates a one line comment
    The next components are the file extensions that we can expect for 
    our language
'''

Python_rules = (
    'Python script', '#',
    'py'
)

C_rules      = (
    'C source file', '//',
    'c'
)

Bash_rules = (
    'Bash script', '#',
    'sh'
)

Lua_rules = (
    'Lua script', '--',
    'lua'
)

# Define more rules here, then add them to 'all_rules'

all_rules = (Python_rules, C_rules, Bash_rules, Lua_rules)


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

name, sqnc = None, None

for rule in all_rules:
    if extn in rule[2:]:
        name, sqnc = rule[0], rule[1]

if name is None:
    print("'%s' is an unknown file extension. Cannot detect it's type for processing." % (extn,))
    exit(-1)

print("Detected next file type:", name)

code = ''

with open(sys.argv[1], 'r') as file:
    file = file.readlines()
    if 'script' in name:
        file = file[1:]
    for line in file:
        code += line

cmnt_jumps = 0
line_idx = 1 + (1 if 'script' in name else 0)
colm_idx = 0

for char_idx in range(len(code)):
    colm_idx+=1
    if cmnt_jumps:
        cmnt_jumps-=1
        continue
    if code[char_idx] in " \t\n":
        if code[char_idx] == '\n':
            line_idx+=1
            colm_idx=0
        continue
    # print(code[char_idx], end='')

    # the 'cmnt_jumps' variable will be used to jump over 
    # chars that don't need to further be analyzed
    # this is useful for languages where in order 
    # to start a 'one-line' comment you need a sequence
    # of multiple chars
    if code[char_idx:char_idx+len(sqnc)] == sqnc:
        cmnt_jumps = len(sqnc)-1
        print("Comment detected at: (%d, %d)" % (line_idx, colm_idx))

print("Program ended")
