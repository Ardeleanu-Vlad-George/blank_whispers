# Purpose
Develope a Python3 script dedicated to reading bash generated source files and printing to the console information about their blank spaces. 
This tool could help you get quicker into old projects and remember what you are supposed to do inside them (yes, some of your projects 
 require you to fill in the blanks of script generated code). 
A 'blank' will literaly be written inside the code, but it can contain extra information regarding where the fill-in needs to take place (
 such as if the fill-in takes place right here over the 'blank', or a couple of lines ahead, or for a certain number of statements after the 
 'blank', etc.).
The 'blank' will be signaled using the already existing syntax for writting one-line comments inside the language, except an extra '? ' 
 sequence is expected right after the comments starting chars to mark it as a 'blank'. Those starting chars can contain anything, even a
 blank space type char like TAB or SPACE, but NO newline, otherwise it doesn't fit the original specifications of the program.
The comment type is deduced from the extension of the file, which must be simple in it's nature: don't use multiple dots for one file 
 ('source.cpp' is fine, 'source.cpp.h' isn't).
The project will contain two directories: './source/' for storing the source code that will be analyzed and './logged/' to which certain 
 outputs of the main file './blank_whispers.py' can be redirected. Considering the purpose of the project, the first one is 'git'-tracked
 while the second isn't.
Find a better way to detect comments and a better way to ignore the 'shebang' in script files. 
