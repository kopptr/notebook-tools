'''
# Example notebook/python script

Markdown cells appear as triple-quoted string literals that do not follow function or class
definitions.

The triple-quote must appear on its own line
'''

#>
# Code cells are denoted by "#>" at the beginning of a line
#
print('Hello, world')

#>
print('O hai, hoomans')

'''
## Notebook-only cells
Code cells that start with "#nb>" will not be executed in the script form of the code
'''

#nb>
#print('Does not get printed in the script')

'''
## Subsection
I can $\LaTeX$
'''

#py>
print('Does not get printed in the notebook')

'''
## sequential markdown cells are cool
'''

#>
print('bar')
