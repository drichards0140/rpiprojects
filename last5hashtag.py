#https://stackoverflow.com/questions/25662144/tweepy-python-retrieving-latest-5-instances-of-a-hashtag
#last 5 of hashtag
import unicodedata
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

search_text = "#irma"
search_number = 2
search_result = api.search(search_text, rpp=search_number)

for i in search_result:
    text_result = unicodedata.normalize('NFKD', i.text).encode('ascii', 'ignore')
    print(text_result)
