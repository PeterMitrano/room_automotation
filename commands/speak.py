from urllib import urlretrieve
import subprocess as sub

#str is the string to be spoken
#priorty 0 is append, 1 is interrupt and kill others

def speak(str,medium="voice"):

	if (medium=="SMS"):
		print 'texting you'
	else:
		print "speaking...",str
		#url='http://www.tts-api.com/tts.mp3?q='+str
		#response=urlretrieve(url,'tts.mp3')
		#sub.call('mpg321 tts.mp3',shell=True)
		sub.call('tts "'+str+'"',shell=True)

if __name__ == '__main__':
	speak("Hello Watson, my name is Sherlock. What can I do for you?",0)
