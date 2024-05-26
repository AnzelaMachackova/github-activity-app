#!/bin/bash

# navigate to the project root directory
cd "$(dirname "$0")/.."

python3 -m venv env

# activate the virtual environment
source env/bin/activate

# instalation dependencies
pip install -r requirements.txt

# run the main application with the GitHub repos passed to the script
python src/main.py "$@"

# deactivating the virtual environment
deactivate

echo "Environment deactivated within the script."