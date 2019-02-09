#!/bin/bash

python-coverage run --branch test.py

python-coverage report -m CodiceFiscale.py > report.txt

python-coverage html CodiceFiscale.py
