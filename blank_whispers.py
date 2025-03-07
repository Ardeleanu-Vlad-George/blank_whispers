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

extn = sys.argv[1].find('.')
if extn == -1:
    print("File doesn't have an extension. Type can't be deduced.")
    exit(-2)

extn = sys.argv[1][extn+1:]

name, sqnc = None, None

for rule in all_rules:
    if extn in rule[2:]:
        name, sqnc = rule[0], rule[1]

if name is None:
    print("'%s' is an unknown file extension. Cannot detect it's type for processing." % (extn,))
    exit(-3)

print("Detected next file type:", name)

code = ''

with open(sys.argv[1], 'r') as file:
    file = file.readlines()
    if 'script' in name:
        file = file[1:]
    for line in file:
        code += line

jump = 0
line = 1 + (1 if 'script' in name else 0)
colm = 0
blank_on = False

# '_' means just the current index, it's as a working variable
for _ in range(len(code)):
    colm+=1

    if jump:
        jump-=1
        continue

    if blank_on:
        print(code[_], end='')
        if code[_] == '\n':
            blank_on = False
        continue

    if code[_] in " \t\n":
        if code[_] == '\n':
            line, colm= line+1, 0
        continue

    if code[_:_+len(sqnc)] == sqnc:
        jump = len(sqnc)-1
        if code[_+jump+1:_+jump+3]=='? ':
            print("Blank detected at: (%d, %d)" % (line, colm), end='\n\t')
            jump+=2
            blank_on=True

print("Program ended")
