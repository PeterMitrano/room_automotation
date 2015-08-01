#
#SMS test via Google Voice
#
#John Nagle
#   nagle@animats.com
#
from googlevoice import Voice
import sys
from bs4 import BeautifulSoup
import json

def extractsms(htmlsms) :
	print "extracting..."
	#accum message items here
	msgitems = []
    	#Extract all conversations by searching for a DIV with an ID at top level.
	tree = BeautifulSoup(htmlsms)
	print "tree",tree
	# parse HTML into tree
	conversations = tree.findAll("div",attrs={"id" : True},recursive=False)
	for conversation in conversations :
	        #For each conversation, extract each row, which is one SMS message.
	        rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
		print "conv",conversation
		# for all rows
	        for row in rows :
			print "row",row
	        	#For each row, which is one message, extract all the fields.
			msgitem = {"id" : conversation["id"]}
			# tag this message with conversation ID
			spans = row.findAll("span",attrs={"class" : True}, recursive=False)
			#for all spans in row
			for span in spans :
				print span["class"]
				cl = str(span["class"]).replace('gc-message-sms-', '')
				#put text in dict
				msgitem[cl] = (" ".join(span.findAll(text=True))).strip()
			msgitems.append(msgitem)
			# add msg dictionary to list
	return msgitems
    
voice = Voice()
voice.login("mitranopeter@gmail.com","ColdplaY1*")

voice.sms()
for msg in extractsms(voice.sms.html):
	print str(msg)
