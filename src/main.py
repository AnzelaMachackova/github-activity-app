import sys
from db_operations import init_db, verify_insert
from github_events import fetch_github_events, calculate_average_time

def main(repositories):
    init_db()  
    for repository in repositories:
        events = fetch_github_events(repository)
        if events:
            print(f"Events fetched and saved successfully for {repository}.")
        else:
            print(f"Failed to fetch or save events for {repository}.")

    verify_insert()
    calculate_average_time()

if __name__ == "__main__":
    repositories = sys.argv[1:]  # getting arguments passed except the first (script name)
    if not repositories:
        print("No repositories provided. Please provide repository names as arguments.")
        sys.exit(1)
    main(repositories)

