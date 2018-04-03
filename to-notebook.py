
import nbformat
import nbformat.v4 as nbf

import sys

pyfile = sys.argv[1]

state = 'between'

cells = []

with open(pyfile, 'r') as f:
    lines = f.readlines()
    cell_str = ''
    for line in lines:
        if state == 'between':
            if line.startswith('#>'):
                state = 'code'
            elif line.startswith("'''"):
                state = 'md'
        elif state == 'code':
            if line.startswith('#>'):
                cells.append(nbf.new_code_cell(cell_str))
                state = 'code'
                cell_str = ''
            elif line.startswith("'''"):
                cells.append(nbf.new_code_cell(cell_str))
                state = 'md'
                cell_str = ''
            else:
                cell_str += line
        elif state == 'md':
            if line.startswith("'''"):
                cells.append(nbf.new_markdown_cell(cell_str))
                state = 'between'
                cell_str = ''
            else:
                cell_str += line
        else:
            print('BAD STATE')
            sys.exit()

nb = nbf.new_notebook()
nb['cells'] = cells
with open('generated_notebook.ipynb', 'w') as f:
    nbformat.write(nb, f)
