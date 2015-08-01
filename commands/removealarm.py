from crontab import CronTab
from node import Node
from command import Command

class RemoveAlarm(Command):

        def removeAlarms(self,translations,medium):
		cron = CronTab(user='pi')
		cron.remove_all()
                return self.tree

        def __init__(self):
		tree = [[ Node( ['remove alarm'], self.removeAlarms) ]]
                Command.__init__(self,tree)

