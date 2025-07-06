# Stephanie Ramos
# July 5, 2025
# Advanced Python
# Module 9.2 Assignment
# APIs

# The purpose of this script is to connect to the Star Wars API, retrieve information about a specific character, and display it in a formatted manner.

import requests
import json

def jprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

url = "http://swapi.py4e.com/api/people/1/"
response = requests.get(url)

print("Status Code:", response.status_code)

print("\nRaw JSON:")
jprint(response.json())

data = response.json()
name = data.get("name")
height = data.get("height")
homeworld = data.get("homeworld")

print("\nFormatted Output: ")
print(f"Name: {name}")
print(f"Height: {height} cm")
print(f"Homeworld URL: {homeworld}")

