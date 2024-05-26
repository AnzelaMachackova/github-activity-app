#!/bin/bash

cd "$(dirname "$0")/.."

python3 -m venv env

# activate the virtual environment
source env/bin/activate
pip install -r requirements.txt

# run the main application with the GitHub repos passed to the script
python src/main.py "$@"

echo "Starting Flask app..."
python src/app.py

echo "Press Ctrl+C to stop app and deactivate environment."
trap 'echo "Stopping Flask server..."; kill $!; echo "Deactivating virtual environment..."; deactivate; echo "Environment closed.";' SIGINT

wait
echo "The end."