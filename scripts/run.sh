#!/bin/bash

# navigate to the project root directory
cd "$(dirname "$0")/.."

# activate the virtual environment
source env/bin/activate

# instalation dependencies
pip install -r requirements.txt

# run the main application
python src/main.py