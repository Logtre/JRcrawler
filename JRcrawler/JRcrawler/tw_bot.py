#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json


### key_word
#keyword = "#bitcoin"
print("何を調べますか?")
keyword = input('>> ')
print('----------------------------------------------------')

### Constants
oath_key_dict = {
    "consumer_key": "VVV4pZ0fMQuRSHx3YGNqfTfPL",
    "consumer_secret": "dnB064KvqMrtNoxyPDS7E9VsVb5IcICXqKxhiiGJywy4J9IPIg",
    "access_token": "1974243638-gwHJed9Npa08fn1DxTjg5QG2f1e72VTKyGUqgkV",
    "access_token_secret": "t1z8poPS4ocYwRbTTu573BqWjpprpRb5NGU0FgrGCPIuY"
}

### Functions
def main():
    tweets = tweet_search(keyword, oath_key_dict)
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        print "tweet_id:", tweet_id
        print "text:", text
        print "created_at:", created_at
        print "user_id:", user_id
        print "user_desc:", user_description
        print "screen_name:", screen_name
        print "user_name:", user_name
    return


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": unicode(search_word),
        "lang": "ja",
        "result_type": "recent",
        "count": "30"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

### Execute
if __name__ == "__main__":
    main()
