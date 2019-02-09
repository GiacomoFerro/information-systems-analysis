#!/bin/bash

rm -f report.txt
python-coverage run --branch test.py
python-coverage report -m CalcoloPasqua.py > report.txt
python-coverage html CalcoloPasqua.py
