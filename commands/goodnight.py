from node import Node
from speak import speak
import random
from command import Command

class Goodnight(Command):
	
        def goodnight(self,trans,medium):
		quotes = ["tomorrow might suck less than today","you are basically a large sac of aqueous solution","the universe cannot plot against you","life is not code, but you should still fix my bugs","WPI is an awesome place full of awesome people","you are not stupid, you just act stupid"]
		speak("goodnight watson, and remember, "+random.choice(quotes),medium)
                return self.tree

        def __init__(self):
		tree = [[ Node( ['goodnight','sleep','go to bed'], self.goodnight) ]]
                Command.__init__(self,tree)
