#! python3

# A program that opens all files in the folder, search for user supplied regular expression and print the result to the screen.

import os
import re

# Write regular expression.
regex = re.compile(r'\s\w\w\w\w\s')

# Open new file to save the result.
with open('result.txt', 'w') as result:

# Change directory to folder with files to check.
    os.chdir('C:\\Users\ogi-8\Desktop\PythonProjects\RegexSearch\FilesToSearch')

# Search files for regular expressions in a for loop and save the match to a new file.
    for file in os.listdir(os.getcwd()):
        print(file)
        text_file = open(file)
        matches = '-'.join(regex.findall(text_file.read()))
        print(matches)
        result.write(matches)

# Print the file with result to the screen.
os.chdir('C:\\Users\ogi-8\Desktop\PythonProjects\RegexSearch')
with open('result.txt') as read_file:
    print(read_file.read())
