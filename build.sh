#!/bin/bash
echo "BUILD START"

# Navigate to the root directory of the project
cd "$(dirname "$0")"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

# upgrade pip
python3.9 -m pip install --upgrade pip

# install all dependencies in the venv
python3.9 -m pip install -r requirements.txt 

# collect static files into the staticfiles directory
python3.9 manage.py collectstatic --noinput

echo "BUILD END"
