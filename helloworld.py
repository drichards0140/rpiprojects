import time
import signal # ?
import scrollphathd
from scrollphathd.fonts import font3x5

scrollphathd.rotate(180) #rotates display for upside down orientation of phathd
scrollphathd.write_string('hello world !!! ', x=0, y=1, font=font3x5, brightness=0.2)
while True:
    scrollphathd.show()
    scrollphathd.scroll()
    time.sleep(0.01) #