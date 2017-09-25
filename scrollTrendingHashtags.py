#!/usr/bin/env python

#https://github.com/tweepy/examples/blob/master/streamwatcher.py
#https://stackoverflow.com/questions/42559155/find-trending-tweets-with-tweepy-for-a-specific-keyword
#https://stackoverflow.com/questions/21203260/python-get-twitter-trends-in-tweepy-and-parse-json

import time
import unicodedata
try:
    import tweepy
except ImportError:
    exit("This script requires the tweepy module\nInstall with: sudo pip install tweepy")
try:
    import scrollphathd
    devEnvironment = False
except:
    devEnvironment = True

#Tweak settings
consumer_key = 'ZlcZeH0QOn7xyUcBPZ6HFDSBp'
consumer_secret = 'dNxjbHYHRM0IZeNIT5BYPnbymb8HeVpZ5tfyCpwBRvc7fOGxma'
access_token = '906925426144108544-gApR442qCAMcapEAZQXxYFCXKMzXQof'
access_token_secret = 'xyL6Z7afLY3eOJZifpyIK2vbD44W9afm0VdkqplRuughP'
debugging = False
apitimer= 60*5 # in seconds
displayrotation = 180
displaybrightness=0.2
displayRewind = True # rapidly displayRewind after the last line
displayScrollSpeed = 0.009 # Delay is the time (in seconds) between each pixel scrolled .02=slowest recommended .004=fastest recommended
displayListLimit = 5 # limit the output of the buffer


def mainLoop():
    output = getTrendingHashtags()
    timeout = time.time() + apitimer #https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
    while True:  
        if devEnvironment:
           scrollConsole(output)
        else:
           scrollDisplay(output)
            
        if time.time() > timeout:
            mainLoop()
            break

def getTrendingHashtags():
    if debugging:
        print('\ngetting api hashtags...')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authorize
    auth.set_access_token(access_token, access_token_secret)#set the access token
    api = tweepy.API(auth) #connect with OAuth
    apitrends = api.trends_place(23424977) #api call to get the top 50 trending items
    trends = apitrends[0]['trends']
    apiresponse = []
    for trend in trends:
        if str(trend['tweet_volume']) == "None":
            apiresponse.append(trend['name']+':0')
        else:
            apiresponse.append(trend['name'] +':'+str(human_format(trend['tweet_volume'])))
    if debugging:
        print("apiresponse")
        print(apiresponse)
    return apiresponse

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.0f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def scrollConsole_old(output):
    #breaks up the output object into displayListLimit sized pieces before sending to the scrolldisplay function, so the buffer will not be over done
    listlength = len(output)
    lastrowstart = (int(listlength / displayListLimit) ) * displayListLimit
    lastrowlength = listlength % displayListLimit
    if devEnvironment:
        print("\nlistlength="+str(listlength)+"\nlastrowlength="+str(lastrowlength)+"\nlastrowstart="+str(lastrowstart))
    
    for x in range(0,listlength,displayListLimit):
        scrollBufferList=[] # clear and set the object
        if x == lastrowstart and lastrowlength!=0:
            endofrow = lastrowlength
        else:
            endofrow = displayListLimit

        for item in range(x,x+endofrow):
            scrollBufferList.append(output[item])

        print("\nScrolling items "+str(x)+" through "+str(x+endofrow))
        print(scrollBufferList) #show the list ofitems to be scrolled
        time.sleep(2) #wait for the items to be scrolled       
    #end for x in range

def scrollConsole(output):
    listlength = len(output)
    lastrowstart = (int(listlength / displayListLimit) ) * displayListLimit
    lastrowlength = listlength % displayListLimit
    if debugging:
        print("\nlistlength="+str(listlength)+"\nlastrowlength="+str(listlength % displayListLimit)+"\nlastrowstart="+str(lastrowstart))
    scrollBufferList=[] # clear and set the object

    for item, val in enumerate(output):
        if (item % displayListLimit) == 0 and item != 0: #if its the size of the limit and not the first item
            scrollBufferList.append(output[item])
            print(scrollBufferList)
            time.sleep(2) #wait for the items to be scrolled 
            scrollBufferList=[] # clear
        elif item == (len(output)-1): #last item in list
            scrollBufferList.append(output[item])
            print(scrollBufferList)
            time.sleep(2) #wait for the items to be scrolled 
            scrollBufferList=[] # clear
        else:
            scrollBufferList.append(output[item])
            
def scrollDisplay(output):
    listlength = len(output)
    lastrowstart = (int(listlength / displayListLimit) ) * displayListLimit
    lastrowlength = listlength % displayListLimit
    scrollBufferList=[] # clear and set the object

    for item, val in enumerate(output):
        if ((item-1) % displayListLimit) == 0 and item != 0: #if its the size of the limit and not the first item
            scrollBufferList.append(output[item])
            if debugging:
                print(scrollBufferList)
            scrollList(scrollBufferList)
            scrollBufferList=[] # clear
        elif item == (len(output)-1): #last item in list
            scrollBufferList.append(output[item])
            if debugging:
                print(scrollBufferList)
            scrollList(scrollBufferList)
            scrollBufferList=[] # clear
        else:
            scrollBufferList.append(output[item])


def scrollList(output):
    #accepts a list of strings and displays to the scrollphat
    #buffer size is limited, suggesting to limit lines < 10, depending on length of each object

    #setup the display default parameters
    scrollphathd.rotate(displayrotation)
    scrollphathd.set_brightness(displaybrightness)
    # displayRewind = True # rapidly displayRewind after the last line
    # delay = 0.009 # Delay is the time (in seconds) between each pixel scrolled
                       
    # Draw each line in lines to the Scroll pHAT HD buffer
    scrollphathd.clear() #clear the buffer before displaying the next list
    line_height = scrollphathd.DISPLAY_HEIGHT + 3 # Determine how far apart each line should be spaced vertically
    offset_left = 0 # Store the left offset for each subsequent line (starts at the end of the last line)
    lengths = [0] * len(output) # Get the length of each 'line' for the buffer
    
    for line, text in enumerate(output):
        lengths[line] = scrollphathd.write_string(text, x=offset_left, y=line_height * line) # scrollphathd.write_string returns the length of the written string in pixels
        offset_left += lengths[line] # we can use this length to calculate the offset of the next line for scrolling effect lateer

    scrollphathd.set_pixel(offset_left - 1, (len(output) * line_height) - 1, 0)  # adds some horizontal/vertical padding to the buffer at the very bottom right of the last line to wrap nice
    scrollphathd.scroll_to(0, 0) # Reset animation
    scrollphathd.show() 

    pos_x = 0 # Keep track of the X and Y position for the displayRewind effect
    pos_y = 0

    for current_line, line_length in enumerate(lengths):
        time.sleep(displayScrollSpeed*10) # Delay a slightly longer time at the start of each line
        for y in range(line_length): # Scroll to the end of the current line
            scrollphathd.scroll(1, 0)
            pos_x += 1
            time.sleep(displayScrollSpeed)
            scrollphathd.show()

        if current_line == len(output) - 1 and displayRewind:  # If on the very last line and displayRewind is True, rapidly scroll back to the first line.
            for y in range(pos_y):
                scrollphathd.scroll(-int(pos_x/pos_y), -1)
                scrollphathd.show()
                time.sleep(displayScrollSpeed)
                scrollphathd.clear() #Clear the buffer

        else: # Otherwise, progress to the next line by scrolling upwards
            for x in range(line_height):
                scrollphathd.scroll(0, 1)
                pos_y += 1
                scrollphathd.show()
    
    time.sleep(displayScrollSpeed)
        #end for x in range

try:
    mainLoop()
   
except KeyboardInterrupt:
    print("Exiting from ctrl+c")
