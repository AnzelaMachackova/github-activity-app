import sys
import logging
import requests
import json
import time
import os
import threading
from db_operations import init_db
from github_events import fetch_github_events
from app import app

def run_flask():
    app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=False)

def fetch_and_save_stats(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open('stats.json', 'w') as f:
            json.dump(data, f)
        logging.info("Statistics fetched and saved successfully.")
    else:
        logging.error(f"Failed to fetch statistics. Status Code: {response.status_code}")

def main(repositories):
    init_db()
    for repository in repositories:
        events = fetch_github_events(repository)
        if events:
            logging.info(f"Events fetched and saved successfully for {repository}.")
        else:
            logging.info(f"Failed to fetch or save events for {repository}.")

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    time.sleep(2)  # few seconds delay to ensure the flask server is up
    fetch_and_save_stats('http://localhost:5001/api/stats')

    logging.info("Stopping Flask server...")
    os._exit(0)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    repositories = sys.argv[1:]  # getting arguments passed except the first (script name)
    if not repositories:
        logging.info("No repositories provided. Please provide repository names as arguments.")
        sys.exit(1)
    main(repositories)

