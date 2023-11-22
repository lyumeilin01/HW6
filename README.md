Input the keyword you want to use in test.json

Navigate to newscover folder
Python3 collector.py -k d89a27d952a942c0bef7d7dc7c28626a -b 31 -i test.json -o output
- use your own api key after -k

run processor.py 
- to get the excel file with all 500 articles and respective features (source:name, title, description)


collector.py
- the page parameter decides which page of result you want out of the pages returned

The sources[country].json file
- contains news sources in us and ca
- which are the two countries representing North America
- these sources are passed as inputs to get articles


