#!/usr/bin/python3
import sys
import io
import re
date = ''
out = ''
author = ''
project = ''
#with open(sys.stdin, 'r', encoding='UTF-8') as file:
input_stream = io.TextIOWrapper(
        sys.stdin.buffer,
        encoding='utf-8',
        errors='backslashreplace')

#sys.stdin.errors = 'backslashreplace';
for line in input_stream:
    if (line.startswith('project')):
        project = line.split(' ')[1].strip()
        continue
    if (line.startswith('Author:')):
#        author = line.split(' ', maxsplit=1)[1].strip()
#        author = re.search(r'[\w\.-]+@[\w\.-]+', line).group(0)
        match = re.search(r'[\w\.-]+@compal\.com', line, re.IGNORECASE)
        author = ''
        if not match: continue
        author = match.group(0).lower()
        continue
    if (line.startswith('Date:')):
        date = line.split(' ', maxsplit=1)[1].strip()
        continue
    if (re.search('\|.*(?:Bin|\d+)', line)):
        if (',' in line): continue
        if not author: continue
        filename, change = [x.strip() for x in line.split('|', maxsplit=1)]
        out += '\t'.join([date, author, project, filename, change]) + '\n'
print("date\tauthor\tproject\tfile\tchange")
print(out)
