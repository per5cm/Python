import json
import requests
import sys
import urllib.parse

# Ensure there is exactly one command-line argument
if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <search term>")

# Encode the search term to handle special characters
search_term = urllib.parse.quote(sys.argv[1])

# Make the API request to iTunes
try:
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={search_term}")
    response.raise_for_status()  # Raise an exception for any HTTP errors
except requests.RequestException:
    sys.exit("Error: Could not retrieve data from iTunes")

# Parse the JSON response
try:
    results = response.json()
except json.JSONDecodeError:
    sys.exit("Error: Could not parse the response as JSON")

# Loop through the results and print track names
for result in results.get("results", []):
    print(result.get("trackName", "Unknown Track"))
