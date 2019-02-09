#!/bin/bash
rm -f report.txt

python-coverage run --branch test.py
python-coverage report -m Irpef.py > report.txt
python-coverage html Irpef.py
