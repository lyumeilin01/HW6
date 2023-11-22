import argparse
import json
import os
from newsapi import fetch_latest_news
from datetime import datetime, timedelta


def main():
    parser = argparse.ArgumentParser(description="News Collector CLI")
    parser.add_argument("-k", "--api-key", required=True, help="NewsAPI API Key")
    #not really needed since we iteratively search until we get 500
    parser.add_argument("-b", "--lookback-days", type=int, default=31, help="Number of days to look back", required=False)

    parser.add_argument("-i", "--input-file", required=True, help="Input JSON file")
    parser.add_argument("-o", "--output-dir", required=True, help="Output directory")

    args = parser.parse_args()


    #combine the sources of us and ca, get a list of source ids, make them a csv string to be used a argument for querying articles

    #with open("sources_us.json", "r") as input_file:
        #source_us = 
    



    with open(args.input_file, "r") as input_file:
        keyword_data = json.load(input_file)

    os.makedirs(args.output_dir, exist_ok=True)

    for name, keywords in keyword_data.items():
        keyword_query = " ".join(keywords)

        end = datetime.today()
        # Format the date as 'YYYY-MM-DD'
        end_date = end.strftime('%Y-%m-%d')

        start = end - timedelta(days=1)
        start_date = start.strftime('%Y-%m-%d')
        count = 0
        i = 0

        
        # start_date = end date- 1 day
        # end_date = today's date
        # get a while loop, while total < 500, keep looking at the previous day
        while count < 500:
            print(f"start date:{start_date}    end_date:{end_date}")

            news = fetch_latest_news(args.api_key, keyword_query, start_date, end_date)
            print(f"length of article: {len(news)}")
            

            output_file_path = os.path.join(args.output_dir, f"{name}_{i}.json")
            with open(output_file_path, "w") as output_file:
                json.dump(news, output_file, indent=4)

            #at the end of while loop
            #if 500 not satisfied
            count+= len(news)
            end = start
            start = end - timedelta(days=1)
            start_date = start.strftime('%Y-%m-%d')
            end_date = end.strftime('%Y-%m-%d')
            i+=1

        
        print("total ", count)    #while loop ends when I have 500 

if __name__ == "__main__":
    main()