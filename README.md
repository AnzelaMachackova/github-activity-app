# GitHub Activity App

## Setup

1. Clone the repository.
2. Run the application: `./scripts/run.sh` with the repositories.
Example: `./scripts/run.sh "AnzelaMachackova/very-running-project" "owid/co2-data" "lucieyarish/huddle-landing-page" "owid/energy-data" "AnzelaMachackova/DBT-Hackathon-2024"`

OR (*?*)
1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python main.py` with the repositories.


## Dev notes: 
- **Proper testing needs to be implemented.**
- To increase the rate limit with the GitHub API, it's better to authenticate requests using an access token. The limit for unauthenticated requests is 60 requests per hour / IP address.