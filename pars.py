#!/usr/bin/python3
import sys
out = ''
author = ''
project = ''
#with open(sys.stdin, 'r', encoding='UTF-8') as file:
for line in sys.stdin:
    if (line.startswith('project')):
        project = line.split(' ')[1].strip()
        continue
    if (line.startswith('Author:')):
        author = line.split(' ', maxsplit=1)[1].strip()
        continue
    if (line.startswith('Date:')):
        date = line.split(' ', maxsplit=1)[1].strip()
        continue
    if ('|' in line):
        if (',' in line): continue
        filename, change = [x.strip() for x in line.split('|')]
        out += '\t'.join([date, author, project + filename, change]) + '\n'
print("date\tauthor\tfile\tchange")
print(out)

