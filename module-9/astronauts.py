# Stephanie Ramos
# July 5, 2025
# Advanced Python
# Module 9.2 Assignment
# APIs

# The purpose of this script is to connect to the Open Notify API, retrieve information about astronauts currently in space, and display it in a formatted manner.
import requests
import json

def jprint(obj):
    """Prints a JSON object in a formatted way."""
    print(json.dumps(obj, indent=4, sort_keys=True))

# GET request to Open Notify API
response = requests.get("http://api.open-notify.org/astros")

# Status code
print(response.status_code)

# unformatted JSON output
jprint(response.json())

# Formatted output
data = response.json()
print(f"\nThere are {data['number']} astronauts in space right now.")
for person in data['people']:
    print(f"{person['name']} on {person['craft']}")
