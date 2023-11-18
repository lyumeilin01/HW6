import argparse
import json
import os
from newsapi import fetch_latest_news

def main():
    parser = argparse.ArgumentParser(description="News Collector CLI")
    parser.add_argument("-k", "--api-key", required=True, help="NewsAPI API Key")
    parser.add_argument("-b", "--lookback-days", type=int, default=30, help="Number of days to look back")
    parser.add_argument("-i", "--input-file", required=True, help="Input JSON file")
    parser.add_argument("-o", "--output-dir", required=True, help="Output directory")

    args = parser.parse_args()



    with open(args.input_file, "r") as input_file:
        keyword_data = json.load(input_file)

    os.makedirs(args.output_dir, exist_ok=True)

    for name, keywords in keyword_data.items():
        keyword_query = " ".join(keywords)
        news = fetch_latest_news(args.api_key, keyword_query, args.lookback_days)

        output_file_path = os.path.join(args.output_dir, f"{name}.json")
        with open(output_file_path, "w") as output_file:
            json.dump(news, output_file, indent=4)

if __name__ == "__main__":
    main()