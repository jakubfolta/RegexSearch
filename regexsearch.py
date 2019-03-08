#! python3

# A program that opens all files in the folder, search for user supplied regular expression and print the result to the screen.

import os
import re

# Write regular expression.
regex = re.compile(r'(\w){4, 5}?\.$')

# Open new file to save the result.
with open('result.txt', 'w') as result:
# Change directory to folder with files to check.
    os.chdir('C:\\Users\ogi-8\Desktop\PythonProjects\RegexSearch\FilesToSearch')
    files = os.listdir('C:\\Users\ogi-8\Desktop\PythonProjects\RegexSearch\FilesToSearch')
    print(os.listdir('C:\\Users\ogi-8\Desktop\PythonProjects\RegexSearch\FilesToSearch'))
    print(os.getcwd())
# TODO: Search files for regular expressions in a for loop and save the match to a new file.
    for file in files:
        print(file) 


# TODO: Print the file with result to the screen.
