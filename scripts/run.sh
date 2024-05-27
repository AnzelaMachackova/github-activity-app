#!/bin/bash

cd "$(dirname "$0")/.."

python3 -m venv env

# activate the virtual environment
source env/bin/activate
pip install -r requirements.txt

# run the main application with the GitHub repos passed to the script
python src/main.py "$@"

# stoping environment
deactivate

echo "The end."