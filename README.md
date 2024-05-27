# GitHub Activity App

This application tracks activities on GitHub for up to five configurable repositories. It calculates statistics based on a rolling window of either 7 days or 500 events, whichever is less, and exposes these statistics through a REST API. This enables users to analyze the average time between consecutive events for different event types and repositories.

## Quick Setup

1. Clone the repository: `git clone https://github.com/AnzelaMachackova/github-activity-app.git`
2. Run the application using the provided shell script: `./scripts/run.sh` with the repositories.

Example: `./scripts/run.sh "AnzelaMachackova/very-running-project" "owid/co2-data" "lucieyarish/huddle-landing-page" "owid/energy-data" "AnzelaMachackova/DBT-Hackathon-2024"`

## Manual Setup

If you prefer manually setting up the environment, follow these steps:

1. Clone the repository: `git clone https://github.com/AnzelaMachackova/github-activity-app.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the main script: `python main.py` with the repositories.

Example: `./scripts/run.sh "AnzelaMachackova/very-running-project" "owid/co2-data" "lucieyarish/huddle-landing-page" "owid/energy-data" "AnzelaMachackova/DBT-Hackathon-2024"`

## Using the API

Once the application is running, it hosts a REST API that provides access to the activity statistics.

### Accessing Statistics

Endpoint: Access the statistics by navigating to: `http://localhost:5001/api/stats`. This endpoint returns and saves JSON data representing the average time between events for each repository and event type being monitored.

## Development Notes

- **Testing: Proper unit and integration tests need to be implemented to ensure reliability.**
- **Authentication:** To increase the rate limit with the GitHub API, it's better to authenticate requests using an access token. The limit for unauthenticated requests is 60 requests per hour / IP address.