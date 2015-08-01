from command import Command
from speak import speak
from node import Node
import time as t

class TellTime(Command):

	def telltime(self,translations,medium):
		speak("it is "+t.strftime("%I:%M %p"),medium)
		return self.tree

        def __init__(self):
		tree=[[  Node(['tell time','what time is it'], self.telltime) ]]
                Command.__init__(self,tree)
			
if __name__ == "__main__":
	TellTime()
