import webbrowser
import datetime

from audio.AUDIO import Say
 
def Tell_Time():
	time = str(datetime.datetime.now())
	# Time will be displayed like this "2020-06-05 17:50:14.582630"
	print(time)
	hour = time[11:13]
	hour = str(int(hour) - 12) if int(hour) > 12 else hour
	min = time[14:16]
	AM_PM = "AM" if int(hour) >= 12 else "PM"
	Say("Currently, it is " + hour + " " + min + " " + AM_PM)	 
	
def Open_Websearch():
	# This method will open the web browser: default is google
	webbrowser.open('www.google.com')

