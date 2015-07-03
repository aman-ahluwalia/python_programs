import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started at " + time.ctime())
while (break_count < total_breaks):
	time.sleep(2*60) //wait time specifying seconds to wait, here it is 2 minutes
	webbrowser.open("http://www.facebook.com/")
	break_count = break_count + 1