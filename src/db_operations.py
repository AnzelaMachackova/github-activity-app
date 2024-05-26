import sqlite3
import csv
import logging

def init_db():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            repo TEXT,
            event_type TEXT,
            created_at TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_event(repo, event_type, created_at):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('INSERT INTO events (repo, event_type, created_at) VALUES (?, ?, ?)',
              (repo, event_type, created_at))
    conn.commit()
    conn.close()

# for testing purposes
def verify_insert():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('SELECT * FROM events')
    result = c.fetchall()
    conn.close()
    if result:
        with open('events.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Repository", "Event Type", "Created At"])
            writer.writerows(result)
        logging.info("Data saved to events.csv")
    else:
        logging.info("Data not found in database.")
