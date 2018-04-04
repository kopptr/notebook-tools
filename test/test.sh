#!/bin/bash

set -e

PYTHON=/usr/local/opt/python/libexec/bin/python

$PYTHON to-script.py test/fixtures/test1.ipynb
cmp generated_script.py test/fixtures/test1.py

$PYTHON to-notebook.py test/fixtures/test1.py
cmp generated_notebook.ipynb test/fixtures/test1.ipynb
