#https://dev.twitter.com/rest/reference/get/trends/place
#This information is cached for 5 minutes. Requesting more frequently than that will not return any more data, and will count against rate limit usage.
#!/usr/bin/env python

import time, sched
import unicodedata
try:
    import tweepy
except ImportError:
    exit("This script requires the tweepy module\nInstall with: sudo pip install tweepy")

#import scrollphathd
#from scrollphathd.fonts import font5x7


# enter your twitter app keys here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
numResults = 5 #1-50 from the default api
scrollSpeed = 0.004 # seconds .02=slowest recommended .004=fastest recommended

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authorize
auth.set_access_token(access_token, access_token_secret)#set the access token
api = tweepy.API(auth) #connect with OAuth
apitrends = api.trends_place(23424977) #api call to get the top 50 trending items

#trends v1
#output = set([trend['name'] for trend in apitrends[0]['trends']])

#trends v2
#trends = apitrends[0]['trends']
#names = [trend['name'] for trend in trends]
#output = ' <> '.join(names)

#v3
#trends  = apitrends[0]['trends']
#names = [trend['name'] for trend in trends]
#output =''
#for x in range(numResults): # just get the first xx instead of the default 50 from the api
#    output += ' <> ' + names[x]

#trends v4 for advscrolling
trends = apitrends[0]['trends']
output=[]
for x in range(numResults):
        output.append(trends[x]['name'] +'-'+str(trends[x]['tweet_volume']))
print(output)
exit()

def mainloop():
    #scrollphathd.clear() #clear the display buffer
    #scrollphathd.show() # put the empty buffer on the display to clear it
    #scrollphathd.rotate(degrees=180)

    while True: #neverending loop
        output_normalized = unicodedata.normalize('NFKD', output).encode('ascii', 'ignore')
        #scrollphathd.write_string(output_normalized, font=font5x7, brightness=0.2) # write to the display
        #output_length = scrollphathd.write_string(output_normalized, font=font5x7, brightness=0.2)
        print(output_normalized)
        time.sleep(0.25)

        #while output_length > 0:
            #scrollphathd.show() 
            #scrollphathd.scroll(1) # scroll the text by x
            #output_length -= 1 # decrement the length of the string to display
            #time.sleep(scrollSpeed) #scroll speed of tweet
    
        #scrollphathd.clear() #clear the display buffer
        #scrollphathd.show() # put the empty buffer on the display to clear it
        time.sleep(15)
        
try:
   mainloop()
   #testloop()

except KeyboardInterrupt:
    print("Exiting from ctrl+c")
