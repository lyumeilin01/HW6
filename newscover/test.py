import unittest
from datetime import datetime
from newscover.newsapi import fetch_latest_news


class NewsAPITestCase(unittest.TestCase):
    def test_no_keywords_provided(self):
        with self.assertRaises(TypeError):
            api_key = "d89a27d952a942c0bef7d7dc7c28626a"
            fetch_latest_news(api_key=api_key)

    def test_lookback_days(self):
        api_key = "d89a27d952a942c0bef7d7dc7c28626a"
        news_keywords = "technology"
        lookback_days = 7
        current_date = datetime.now()
        articles = fetch_latest_news(api_key, news_keywords, lookback_days)
        for article in articles:
            published_at = datetime.fromisoformat(article["publishedAt"][:-1])  
            time_difference = current_date - published_at
            self.assertLessEqual(time_difference.days, lookback_days)

    def test_non_alphabetic_keyword(self):
        api_key = "d89a27d952a942c0bef7d7dc7c28626a"

        with self.assertRaises(ValueError):
            fetch_latest_news(api_key=api_key, news_keywords="technology123")

if __name__ == "__main__":
    unittest.main()
