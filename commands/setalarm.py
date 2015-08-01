from crontab import CronTab
from node import Node
from command import Command
from speak import speak
import re

class SetAlarm(Command):

        def setTime(self,translations,medium):#0,0
		for trans in translations:
			m=re.search("([0-9]+):?([0-9]+)?\s([ap]\.?m\.?)",trans)
			if m:
				self.hr=int(m.group(1))
				if (m.group(2)>0):
					self.min=int(m.group(2))
				else:
					self.min=0
				self.period=m.group(3)
				speak("creating an alarm for"+m.group(0)+". is that correct?",medium)
				self.tree[1][0].openNode()
				self.tree[1][1].openNode()
				return self.tree
		say("not valid alarm time found",medium)
                return self.tree


	def affirmTime(self,translations,medium):#1,0
		speak("ok, creating alarm now",medium)
		cron = CronTab(user='pi')
		job=cron.new(command="sudo /home/pi/Room/commands/alarm.sh")
		job.minute.on(self.min)
		job.hour.on(self.hr)
		if job.is_valid():
			job.enable()
			cron.write()
			Node.closeAll(self.tree)
			return self.tree
		else:
			speak("error creating cron job. peter fix me. I hate being quasi functional.",medium)
                return self.tree


	def daffirmTime(self,translations,medium):#1,1
		speak("sorry, say that again please. I promise i'll figure it out this time.",medium)
		Node.closeAll(self.tree)
                return self.tree
	
	def __init__(self):
		base = Node( ['set alarm for','create alarm for'], self.setTime)
		affirmTime = Node( ['yes','correct'], self.affirmTime)
		daffirmTime = Node( ['no','incorrect'], self.daffirmTime)
		tree = [ [base] , [affirmTime,daffirmTime] ]
                Command.__init__(self,tree)

