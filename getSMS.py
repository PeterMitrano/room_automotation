from googlevoice import Voice,util
from bs4 import BeautifulSoup
import json
import re
from time import sleep

def getSMS(queue):

	voice = Voice()
	print "logging in..."
	voice.login("mitranopeter@gmail.com","ColdplaY1*")
	print "logged in..."


	while True:	
		#sleep(60)
		voice.sms()
		tree = BeautifulSoup(voice.sms.html)
		unread = tree.find("div",attrs={"class":"goog-flat-button gc-message gc-message-unread gc-message-sms"})
		try:
			thread = unread.find("div",attrs={"class":"gc-message-message-display"})
			rows = thread.findAll("div",attrs={"class":"gc-message-sms-row"})
			row=rows[len(rows)-1]
			sender = ''.join(row.find("span",attrs={"class":"gc-message-sms-from"}))
			if re.search("Watson",sender):
				message = ''.join(row.find("span",attrs={"class":"gc-message-sms-text"})).strip(' \t\r\n')
				message = "Sherlock "+message
				print 'putting',message
				queue.put(message)
				#indicate this came from sms
				queue.put("SMS")
			print 'marking as read'
			while True:
				folder = voice.search('is:unread')
				if folder.totalSize <= 0 :
					break
				for message in folder.messages:
					message.mark(1)
			print 'done marking as read'
		except:
			return
