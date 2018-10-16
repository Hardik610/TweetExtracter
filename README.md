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
- `contains` : Facilitates full-text search
- `wildcard` :
    * `startswith` : *substring
    * `endswith` : substring*
    * `wildcard` : *substring*
- `gte` : '>=' operator for numeric/datetime values
- `gt` : '>' operator for numeric/datetime values
- `lte` : '<=' operator for numeric/datetime values
- `lt` : '<' operator for numeric/datetime values

**Pagination** is done by the parameters `from` and `size` as it is used in ElasticSearch.
**AND represents must, OR repesents should and NOT repesents must_not, as matched according to elasticsearch query attributes.**

API2 - `http://0.0.0.0:8080/API2?from=0&size=10
`
###### Body in Raw
```
{
    "sort":["created_at"],              
    "criteria": {
        "OR": [
            {
            "fields": ["tweet_text"],
            "operator": "contains",
            "query": "PM"
            }
        ]
    }
}
```
###### Response
```
{
    "count": {
        "fetched": 20,
        "total": 35
    },
    "results": [
        {
            "_id": "AWZ34T6urOtk92tX3kg4",
            "_index": "tweets_index",
            "_score": null,
            "_source": {
                "country": "",
                "country_code": "",
                "created_at": "2018-10-15T13:19:01",
                "favorite_count": 0,
                "hashtags": [],
                "is_retweeted": false,
                "lang": "en",
                "location": "Bangalore",
                "reply_count": 0,
                "retweet_count": 0,
                "screen_name": "NdSolanki",
                "source_device": "Twitter for iPhone",
                "timestamp_ms": "1539609541073",
                "tweet_text": "RT @SmokingSkills_: Who praises Modi?\n\n- World Bank\n- British PM  \n- Saudi Arabia\n\nWho makes fun of Modi\n- Pidi comedians\n- The Wire \n- Ser…",
                "user_name": "Narendra Solanki"
            },
            "_type": "tweet",
            "sort": [
                1539609541000
            ]
        },
        {.....}
        {.....}
        {.....}
        {.....}
    ]
}
```
# 3. API to export filtered data as CSV

API3 - `http://0.0.0.0:8080/API3` (Method supported - 'GET', 'POST')

Input should be given in the same format as given in API2. CSV file will be downloaded when puts request on browser. When posted in postman application csv data will be reflected in response body and you can find attachment in header.
