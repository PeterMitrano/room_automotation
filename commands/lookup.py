import wikipedia
from node import Node
from speak import speak
import sys
from command import Command

class LookUp(Command):

        def lookUp(self,translations,medium):
		try:
			for trans in translations:
				m=trans.search("(look up|wikipedia)\s(.*)",trans)
				if m:
					self.term=m.group(2)
					speak(wikipedia.summary(self.term,sentences=1),medium)
		except:
			speak("sorry. I couldnt find an article on "+term,medium)
                return self.tree

	def __init__(self):
		tree = [[ Node( ['look up','wikipedia'], self.lookUp) ]]
                Command.__init__(self,tree)
