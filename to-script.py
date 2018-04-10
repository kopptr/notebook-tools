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

with open(args.target, 'w') as f:
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            f.write("'''\n")
            f.write(''.join(cell['source']))
            f.write("\n'''\n\n")
        elif cell['cell_type'] == 'code':
            if cell['source'].startswith('#nb>'):
                f.write(cell['source'].replace('\n', '\n#') + '\n\n')
            else:
                f.write('#>\n')
                f.write(''.join(cell['source']) + '\n\n')

