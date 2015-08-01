from speak import speak
from node import Node
from crontab import CronTab
from command import Command


class ListAlarms(Command):

        def listAlarms(self,translations,medium):
		cron = CronTab(user='pi')
		speak('you have alarms set for',medium)
		for job in cron:
			hr = job.hour.parts[0]
			min = job.minute.parts[0]
			period="am"
			if hr>12:
				hr=hr-12	
				period="pm"
			speak(str(hr)+":"+str(min)+" "+period,medium)
                return self.tree
	
        def __init__(self):
		tree=[[ Node( ['list alarms'], self.listAlarms) ]]
                Command.__init__(self,tree)
