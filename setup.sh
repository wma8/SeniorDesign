#!/bin/bash

# rhel specific command to activate python 3.6
source /opt/rh/rh-python36/enable

# install virtualenv if not yet installed
python -m pip install virtualenv --user

# initialize the virtual environment
virtualenv venv

# activate the virtual environment
source venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install all dependencies listed in requirements.txt
pip install -r requirements.txt

# deactivate the virtual environment
deactivate

echo "setup complete"
