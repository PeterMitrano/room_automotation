from command import Command
from node import Node
from speak import speak

#make lights go nuts
#make fan go nuts
#play music

class Party(Command):

        def party(self,translations,medium):
		speak("You got it Watson. It's party time party",medium)
                return self.tree
		

        def __init__(self):
		tree = [[ Node( ['party'], self.party) ]]
                Command.__init__(self,tree)
