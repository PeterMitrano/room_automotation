from node import Node
from command import Command
from speak import speak
import re
import random

class SayHello(Command):

        def greet(self,translations,medium):
		for trans in translations:
			m=re.search("say hello to (.*)",trans)
			if m:
				name=m.group(2)
				print "name",name
				compliments=["damn sexy","drop dead gorgous","stunning","absolutely incredible","ravishing","amazing","beautiful"]
				speak("Hello "+name+". you're looking "+random.choice(complements)+" today",medium)
				return self.tree
		speak("you didn't tell me who you're introducing me to",medium)
                return self.tree
	

	def __init__(self):
		tree = [[ Node( ['say hello to'], self.greet) ]]
                Command.__init__(self,tree)

