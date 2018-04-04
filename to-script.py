import nbformat
import nbformat.v4 as nbf

import sys

nbfile = sys.argv[1]

with open(nbfile, 'r') as f:
    nb = nbformat.read(f, 4)

with open('generated_script.py', 'w') as f:
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            f.write("'''\n")
            f.write(''.join(cell['source']))
            f.write("'''\n\n")
        elif cell['cell_type'] == 'code':
            f.write('#>\n')
            f.write(''.join(cell['source']))

