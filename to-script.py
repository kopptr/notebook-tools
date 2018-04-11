#!/usr/bin/env python3
import argparse
import nbformat
import nbformat.v4 as nbf

import sys

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('target', nargs='?', default='')
args = parser.parse_args()
if args.target == '':
    args.target = args.source.replace('.ipynb', '.py')

with open(args.source, 'r') as f:
    nb = nbformat.read(f, 4)

first = True
with open(args.target, 'w') as f:
    for cell in nb['cells']:
        if first:
            first = False
        else:
            f.write('\n')
        if cell['cell_type'] == 'markdown':
            f.write("'''\n")
            f.write(''.join(cell['source']))
            f.write("\n'''\n")
        elif cell['cell_type'] == 'code':
            if cell['source'].startswith('#nb>'):
                f.write(cell['source'].replace('\n', '\n#') + '\n')
            elif cell['source'].startswith('#py>'):
                f.write('#py>\n' + '\n'.join([x[1:] for x in cell['source'].split('\n')[1:]]) + '\n')
            else:
                f.write('#>\n')
                f.write(''.join(cell['source']) + '\n')

