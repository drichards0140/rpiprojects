#https://stackoverflow.com/questions/42559155/find-trending-tweets-with-tweepy-for-a-specific-keyword
#https://stackoverflow.com/questions/21203260/python-get-twitter-trends-in-tweepy-and-parse-json

import unicodedata
import json
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#https://dev.twitter.com/rest/reference/get/trends/place
#woeidlookup.com united states
trends1 = api.trends_place(23424977) 

search_hashtag = tweepy.Cursor(api.search, q='irma').items(3)
for tweet in search_hashtag:
    print(unicodedata.normalize('NFKD', tweet.text).encode('ascii', 'ignore'))

data = trends1[0] # grab the trends
trends = data['trends']# grab the name from each trend
names = [trend['name'] for trend in trends]# put all the names together with a ' ' separating them
trendsName = ' | '.join(names)
print(print(unicodedata.normalize('NFKD', trendsName).encode('ascii', 'ignore')))
