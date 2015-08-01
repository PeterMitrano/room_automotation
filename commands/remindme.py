from speak import speak
from crontab import CronTab
from node import Node
from command import Command
import re

class RemindMe(Command):

        def remind1(self,translations,medium):#0,0
		speak("what should I remind you of?",medium)
		self.tree[1][0].openNode() #setMessage
                return self.tree

 
	def remind2(self,translations,medium):#0,1
		for trans in translations:
			if re.search("remind me.*",trans):
				self.message=re.sub(".*remind me","",trans)
				print 'message:',self.message
				speak("message is.  "+self.message+". is that correct?",medium)
				self.tree[2][0].openNode() #affirmMessage
				self.tree[2][1].openNode() #daffirmMessage
				return self.tree
		speak("reminder not understood. error in remind2",medium)
                return self.tree

	def setMessage(self,translations,medium):#1,0
		for trans in translations:
			if re.search("(set message to)(.*)",trans):
				self.message=re.sub("set message to","",trans)
				print 'message:',self.message
				speak("message is "+self.message+". is that correct?",medium)
				self.tree[1][0].closeNode() #setMessage
				self.tree[2][0].openNode() #affirmMessage
				self.tree[2][1].openNode() #daffirmMessage
				return self.tree
		speak("reminder not understood. error in set message",medium)
                return self.tree

	def setTime(self,translations,medium):#1,1
		for trans in translations:
			time=re.search("([0-9]+):?([0-9]*)\s([ap]\.?m\.?)",trans)
			if time:
				self.hr=time.group(1)
				self.min=time.group(2)
				self.period=time.group(3)
				speak("reminder set for "+time.group(0)+" . is that correct?",medium)
				print self.hr," : ",self.min," ",self.period
				self.tree[1][1].closeNode() #setTime
				self.tree[2][2].openNode() #affirmTimme
				self.tree[2][3].openNode() #daffirmTimme
				return self.tree
		speak("time not understood. error in set time",medium)
                return self.tree

	def affirmMessage(self,translations,medium):#2,0
		speak("ok, saving message. when do you want to set this reminder for?",medium)
		self.tree[2][0].closeNode() #affirmMessage
		self.tree[2][1].closeNode() #daffirmMessage
		self.tree[1][1].openNode() #setTime
                return self.tree

	def daffirmMessage(self,translations,medium):#2,1
		speak("sorry. please state message again",medium)
		self.tree[2][0].closeNode() #daffrmMessage
		self.tree[2][1].closeNode() #daffrmMessage
		self.tree[1][0].openNode() #setMessage
                return self.tree

	def affirmTime(self,translations,medium):#2,2
		speak("ok, saving reminder. should I text you this reminder?",medium)
		self.tree[2][2].closeNode()#affirmTime
		self.tree[2][3].closeNode()#daffirmTime
		self.tree[3][0].openNode()#yesText
		self.tree[3][1].openNode()#noText
                return self.tree

	def daffirmTime(self,translations,medium):#2,3
		speak("sorry. please state time again",medium)
		self.tree[2][3].closeNode() #daffirmTime
		self.tree[1][1].openNode() #setTime
                return self.tree

	def yesText(self,translations,medium):
		speak("ok great. glad that is over. I will text you this reminder",medium)
		Node.closeAll(self.tree)
                return self.tree

	def noText(self,translations,medium):	
		speak("Ok, I'll just tell you.",medium)
		Node.closeAll(self.tree)
                return self.tree

	def __init__(self):
		base1 = Node( ['set reminder'], self.remind1)
		base2 = Node( ['remind me'], self.remind2)

		message = Node( ['set message to'], self.setMessage)
		time = Node( ['set time to'], self.setTime)

		affirmTime = Node( ['yes'], self.affirmTime)
		daffirmTime = Node( ['no'], self.daffirmTime)
		affirmMessage = Node( ['yes'], self.affirmMessage)
		daffirmMessage = Node( ['no'], self.daffirmMessage)

		yesText = Node( ['yes'], self.yesText)
		noText = Node( ['no'], self.noText)

		tree = [[ base1,base2 ],[message,time],[affirmMessage,daffirmMessage,affirmTime,daffirmTime],[yesText,noText]]
                Command.__init__(self,tree)

