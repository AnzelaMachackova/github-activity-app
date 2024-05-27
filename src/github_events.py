import requests
import time
import sqlite3
from datetime import datetime, timedelta
from db_operations import save_event
import logging

def fetch_github_events(repository, max_retries=5):
    base_url = f"https://api.github.com/repos/{repository}/events"
    retry_count = 0
    backoff_factor = 2  

    while retry_count < max_retries:
        response = requests.get(base_url)
        if response.status_code == 200:
            events = response.json()
            for event in events:
                save_event(event['repo']['name'], event['type'], event['created_at'])
            logging.info("Data saved to database")
            return events
        elif response.status_code == 403:
            if "X-RateLimit-Reset" in response.headers:
                reset_time = int(response.headers['X-RateLimit-Reset'])
                delay = max(0, reset_time - int(time.time())) + backoff_factor ** retry_count
                logging.info(f"Rate limit exceeded. Waiting {delay} seconds to retry...")
                time.sleep(delay)
                retry_count += 1
            else:
                logging.info("Rate limit exceeded but no reset time provided")
                break
        else:
            logging.info(f"Failed to fetch events: HTTP {response.status_code} - {response.reason}")
            break

    logging.info("Max retries exceeded, unable to fetch data.")

def calculate_average_time(db_path='events.db', days=7, max_events=500):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    time_limit = datetime.now() - timedelta(days=days)
    query = """
    SELECT repo, event_type, created_at
    FROM events
    WHERE timestamp >= ?
    ORDER BY repo, event_type, created_at
    LIMIT ?
    """
    cursor.execute(query, (time_limit.strftime('%Y-%m-%dT%H:%M:%SZ'), max_events))
    
    last_repo = None
    last_event_type = None
    last_created_at = None
    time_differences = []
    averages = []

    for repo, event_type, created_at in cursor.fetchall():
        created_at_dt = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
        if repo == last_repo and event_type == last_event_type:
            time_diff = (created_at_dt - last_created_at).total_seconds() / 60  # minutes
            time_differences.append(time_diff)
        else:
            if last_repo is not None and time_differences:
                avg_time_diff = sum(time_differences) / len(time_differences)
                averages.append({
                    "repository": last_repo,
                    "event_type": last_event_type,
                    "average_time_minutes": avg_time_diff
                    })
                time_differences = []
        
        last_repo = repo
        last_event_type = event_type
        last_created_at = created_at_dt

    if time_differences:
        avg_time_diff = sum(time_differences) / len(time_differences)
        averages.append({
            "repository": last_repo,
            "event_type": last_event_type,
            "average_time_minutes": avg_time_diff
            })
    
    conn.close()
    
    return averages