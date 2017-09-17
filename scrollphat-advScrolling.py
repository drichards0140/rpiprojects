#!/usr/bin/env python

import time
import scrollphathd
try:
    import tweepy
except ImportError:
    exit("This script requires the tweepy module\nInstall with: sudo pip install tweepy")

print("""
Scroll pHAT HD: Advanced Scrolling
Advanced scrolling example which displays a message line-by-line
and then skips back to the beginning.
Press Ctrl+C to exit.
""")


scrollphathd.rotate(180)
scrollphathd.set_brightness(0.2)
rewind = True# rapidly rewind after the last line
delay = 0.009 # Delay is the time (in seconds) between each pixel scrolled
line_height = scrollphathd.DISPLAY_HEIGHT + 3 # Determine how far apart each line should be spaced vertically
offset_left = 0 # Store the left offset for each subsequent line (starts at the end of the last line)

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
trends = apitrends[0]['trends']
lines=[]
for x in range(numResults):
        lines.append(trends[x]['name'] +'-'+str(trends[x]['tweet_volume']))
print(lines)


# Change the lines below to your own message
#lines = ["And we'll make things 1",
#         "And we'll break things 2",
#         "'til we're altogether aching 3"]

# Draw each line in lines to the Scroll pHAT HD buffer
# scrollphathd.write_string returns the length of the written string in pixels
# we can use this length to calculate the offset of the next line
# and will also use it later for the scrolling effect.
lengths = [0] * len(lines)

for line, text in enumerate(lines):
    lengths[line] = scrollphathd.write_string(text, x=offset_left, y=line_height * line)
    offset_left += lengths[line]

# adds a little bit of horizontal/vertical padding into the buffer at the very bottom right of the last line to keep things wrapping nicely.
scrollphathd.set_pixel(offset_left - 1, (len(lines) * line_height) - 1, 0)

while True:
    # Reset the animation
    scrollphathd.scroll_to(0, 0)
    scrollphathd.show()

    # Keep track of the X and Y position for the rewind effect
    pos_x = 0
    pos_y = 0

    for current_line, line_length in enumerate(lengths):
        # Delay a slightly longer time at the start of each line
        time.sleep(delay*10)

        # Scroll to the end of the current line
        for y in range(line_length):
            scrollphathd.scroll(1, 0)
            pos_x += 1
            time.sleep(delay)
            scrollphathd.show()

        # If we're currently on the very last line and rewind is True
        # We should rapidly scroll back to the first line.
        if current_line == len(lines) - 1 and rewind:
            for y in range(pos_y):
                scrollphathd.scroll(-int(pos_x/pos_y), -1)
                scrollphathd.show()
                time.sleep(delay)

        # Otherwise, progress to the next line by scrolling upwards
        else:
            for x in range(line_height):
                scrollphathd.scroll(0, 1)
                pos_y += 1
                scrollphathd.show()
time.sleep(delay)
