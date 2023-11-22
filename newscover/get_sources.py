import requests
import json

base_url = "https://newsapi.org/v2/top-headlines/sources"
api_key = "d89a27d952a942c0bef7d7dc7c28626a"

params = {
    "language": "en",
    "apiKey": api_key,
    #"page": 1, #altered from 1 to 5 to collect result from 5 pages
    #"sources":
    "country": "ca"
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
  # Parse the JSON data in the response
  data = response.json()

  # Access the 'sources' key in the JSON response
  sources = data["sources"]

  # Print the list of sources


  with open("sources_ca.json", "w") as output_file:
        json.dump(sources, output_file, indent = 4)
