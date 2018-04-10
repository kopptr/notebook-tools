#!/bin/bash

set -e

PYTHON=/usr/local/opt/python/libexec/bin/python

$PYTHON to-script.py test/fixtures/test1.ipynb generated_script.py
cmp generated_script.py test/fixtures/test1.py

$PYTHON to-notebook.py test/fixtures/test1.py generated_notebook.ipynb
cmp generated_notebook.ipynb test/fixtures/test1.ipynb

rm generated_notebook.ipynb generated_script.py
