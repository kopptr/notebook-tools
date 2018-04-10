import argparse
import nbformat
import nbformat.v4 as nbf

import sys

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('target', nargs='?', default='')
args = parser.parse_args()
if args.target == '':
    args.target = args.source.replace('.py', '.ipynb')

state = 'between'

cells = []

with open(args.source, 'r') as f:
    lines = f.readlines()
    cell_str = ''
    for line in lines:
        if state == 'between':
            if line.startswith('#>'):
                state = 'code'
            elif line.startswith('#nb>'):
                state = 'nbonlycode'
                cell_str = '#nb>\n'
            elif line.startswith('#py>'):
                state = 'pyonlycode'
                cell_str = '#py>\n'
            elif line.startswith("'''"):
                state = 'md'
        elif state == 'code':
            if line.startswith('#>'):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'code'
                cell_str = ''
            elif line.startswith('#nb>'):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'nbonlycode'
                cell_str = '#nb>\n'
            elif line.startswith('#py>'):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'pyonlycode'
                cell_str = '#py>\n'
            elif line.startswith("'''"):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'md'
                cell_str = ''
            else:
                cell_str += line
        elif state == 'md':
            if line.startswith("'''"):
                cells.append(nbf.new_markdown_cell(cell_str.strip()))
                state = 'between'
                cell_str = ''
            else:
                cell_str += line
        elif state == 'nbonlycode':
            if line.startswith('#>'):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'code'
                cell_str = ''
            elif line.startswith('#nb>'):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'nbonlycode'
                cell_str = '#nb>\n'
            elif line.startswith('#py>'):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'pyonlycode'
                cell_str = '#py>\n'
            elif line.startswith("'''"):
                cells.append(nbf.new_code_cell(cell_str.strip()))
                state = 'md'
                cell_str = ''
            else:
                cell_str += line[1:]
        elif state == 'pyonlycode':
            if line.startswith('#>'):
                cells.append(nbf.new_code_cell(cell_str.strip()[:-2]))
                state = 'code'
                cell_str = ''
            elif line.startswith('#nb>'):
                cells.append(nbf.new_code_cell(cell_str.strip()[:-2]))
                state = 'nbonlycode'
                cell_str = '#nb>\n'
            elif line.startswith('#py>'):
                cells.append(nbf.new_code_cell(cell_str.strip()[:-2]))
                state = 'pyonlycode'
                cell_str = '#py>\n'
            elif line.startswith("'''"):
                cells.append(nbf.new_code_cell(cell_str.strip()[:-2]))
                state = 'md'
                cell_str = ''
            else:
                cell_str += '#' + line

        else:
            print('BAD STATE')
            sys.exit()
    if state == 'code' and cell_str != '':
        cells.append(nbf.new_code_cell(cell_str.strip()))


nb = nbf.new_notebook()
nb['cells'] = cells
with open(args.target, 'w') as f:
    nbformat.write(nb, f)
