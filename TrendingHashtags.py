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
apitrends = api.trends_place(23424977)

trends = set([trend['name'] for trend in apitrends[0]['trends']])
for trend in trends:
    print(trend)

#data = apitrends[0] # grab the trends object
#trends = data['trends']# grab the name from each trend
#names = [trend['name'] for trend in trends]# put all the names together with a ' ' separating them
#allTrends = ' | '.join(names)
#print(print(unicodedata.normalize('NFKD', allTrends).encode('ascii', 'ignore')))

