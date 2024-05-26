import sys
from db_operations import init_db
from github_events import fetch_github_events
import logging

def main(repositories):
    init_db()  
    for repository in repositories:
        events = fetch_github_events(repository)
        if events:
            logging.info(f"Events fetched and saved successfully for {repository}.")
        else:
            logging.info(f"Failed to fetch or save events for {repository}.")

if __name__ == "__main__":
    repositories = sys.argv[1:]  # getting arguments passed except the first (script name)
    if not repositories:
        logging.info("No repositories provided. Please provide repository names as arguments.")
        sys.exit(1)
    main(repositories)

