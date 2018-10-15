# TweetExtracter
APIs created to store Twitter Streaming Data and retreive data after applying filters. So it consist of 3 APIs:-
1. API to trigger Twitter Stream
2. API to filter stored data
3. API to export filtered data as CSV

### Built With
1. Python
2. Flask
3. ElasticSearch
4. Tweepy

# Setup Project(Installation Instruction)
1. clone the project
2. cd to project folder `cd TweetExtracter`
3. create virtual environment `virtualenv venv` and activate it `source venv/bin/activate`
4. Install requirements `pip install -r requirements.txt`
5. Change the twitter stream API credentials in configure.py file.

# Setup ElasticSearch (Installation Instruction)
To install and configure follow the given link of where all steps are clearly given:-
`https://www.tutorialspoint.com/articles/install-and-configure-elasticsearch-in-ubuntu-14-04-3`

# To Run Server
Run the `python server.py`

# 1.API to trigger Twitter Stream

This API trigger twitter streaming and stores the data by Twitter Streaming API. The Streaming can be done:-
`http://0.0.0.0:8080/API1?keywords=modi,AbkiBarModiSarkar,ModiForPM`

Where keywords can be any keyword for which streaming needs to be performed. Successful response
```
{
    "message": "Started streaming tweets with keywords [u'modi', u'AbkiBarModiSarkar', u'ModiForPM']",
    "status": "success"
}
```
# 2. API to filter stored data
This API fetches stored data by first API based on filters and search keywords and sort them as required.

**Operators:** Following operators are available:-
- `equals`: for exact match or equal for numeric value
