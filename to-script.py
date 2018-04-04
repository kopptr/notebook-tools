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
            f.write("\n'''\n\n")
        elif cell['cell_type'] == 'code':
            if cell['source'].startswith('#nb>'):
                f.write(cell['source'].replace('\n', '\n#') + '\n\n')
            else:
                f.write('#>\n')
                f.write(''.join(cell['source']) + '\n\n')

