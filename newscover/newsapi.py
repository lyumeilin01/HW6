import requests
import datetime
import re
from pathlib import Path
import json



def fetch_latest_news(api_key, news_keywords, start_date, end_date):
    #if re.search(r'[^a-zA-Z]', news_keywords) is not None:
        #raise ValueError()
    
    base_url = "https://newsapi.org/v2/everything/"

    #lookback day by day, I think 5 pages is the maximum for display
    # params = {
    #     "q": news_keywords,
    #     "language": "en",
    #     "from": (datetime.datetime.now() - datetime.timedelta(days=lookback_days)).isoformat(),
    #     "to": datetime.datetime.now().isoformat(),
    #     "apiKey": api_key,
    #     #"page": 1, #altered from 1 to 5 to collect result from 5 pages
    #     #"sources":

    # }

    #get a string of north american sources

    uspath = Path(__file__).parent.parent / "sources_us.json"
    capath = Path(__file__).parent.parent / "sources_ca.json"
    with open (uspath, "r") as json_data:
        content = json.load(json_data)
        id_list = [item["id"] for item in content]
        comma_separated_ids = ",".join(id_list)
        us_sources = comma_separated_ids
    #print(us_sources)

    with open (capath, "r") as json_data:
        content = json.load(json_data)
        id_list = [item["id"] for item in content]
        comma_separated_ids = ",".join(id_list)
        ca_sources = comma_separated_ids
    tgt = f"{us_sources},{ca_sources}"


    sources = tgt
    params = {
        "q": news_keywords,
        "language": "en",
        "from": start_date, #"2023-11-22"
        "to": end_date,
        "apiKey": api_key,
        #"page": 1, #altered from 1 to 5 to collect result from 5 pages
        "sources": sources

    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        return articles
    else:
        print("Error fetching news:", response.status_code)
        return []





# api_key = "d89a27d952a942c0bef7d7dc7c28626a"
# news_keywords = "technology"
# latest_news = fetch_latest_news(api_key, news_keywords, 1)
# print(latest_news)
