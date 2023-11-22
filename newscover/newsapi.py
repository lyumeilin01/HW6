import requests
import datetime
import re


base_url = "https://newsapi.org/v2/top-headlines/sources"
api_key = "d89a27d952a942c0bef7d7dc7c28626a"

params = {
    "language": "en",
    "apiKey": api_key,
    #"page": 1, #altered from 1 to 5 to collect result from 5 pages
    #"sources":
    "country": "us, ca"
}
def fetch_latest_news(api_key, news_keywords, lookback_days=31):
    #if re.search(r'[^a-zA-Z]', news_keywords) is not None:
        #raise ValueError()
    
    base_url = "https://newsapi.org/v2/everything/"

    #lookback day by day, I think 5 pages is the maximum for display
    params = {
        "q": news_keywords,
        "language": "en",
        "from": (datetime.datetime.now() - datetime.timedelta(days=lookback_days)).isoformat(),
        "to": datetime.datetime.now().isoformat(),
        "apiKey": api_key,
        #"page": 1, #altered from 1 to 5 to collect result from 5 pages
        #"sources":

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
