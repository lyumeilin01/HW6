import requests
import json

base_url = "https://newsapi.org/v2/top-headlines/sources"
api_key = "d89a27d952a942c0bef7d7dc7c28626a"

params = {
    "language": "en",
    "apiKey": api_key,
    #"page": 1, #altered from 1 to 5 to collect result from 5 pages
    #"sources":
    "country": "us, ca"
}

response = requests.get(base_url, params=params)

print(response.json().get("sources"))

#with open("sources.json", "w") as output_file:
      #json.dump(response.json(), output_file, indent = 4)
