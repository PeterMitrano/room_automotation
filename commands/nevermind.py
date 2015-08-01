from speak import speak
from node import Node
from command import Command

class Nevermind(Command):

        def respond(self,translations,medium):
		speak("ok Watson, whenever you're ready",medium)
                return self.tree

        def __init__(self):
		tree=[[ Node( ['nevermind','forget it'], self.respond) ]]
                Command.__init__(self,tree)

