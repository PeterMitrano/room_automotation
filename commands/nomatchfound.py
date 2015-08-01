from speak import speak
from node import Node
from command import Command

class NoMatchFound(Command):

        def nomatch(self,translations,medium):
		speak("Hello Watson, what can I do for you?",medium)
		return self.tree

        def __init__(self):
		tree = [[ Node( ['Sherlock'], self.nomatch) ]]
                Command.__init__(self,tree)

