from speak import speak
from node import Node
from command import Command

class ListCommands(Command):

        def listCommands(self,translations,medium):
		speak("commands are",medium)
		for line in open("/home/pi/Room/commands/__init__.py"):
			line=line.split(" ")[1]
			speak(line,medium)
		return self.tree

        def __init__(self):
		tree = [[ Node( ['list commands'], self.listCommands) ]]
                Command.__init__(self,tree)
