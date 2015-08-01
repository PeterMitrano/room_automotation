from speak import speak
from node import Node
from command import Command
import random


class ThankYou(Command):

        def thanks(self,translations,medium):
		responses = ['no, thank you,  babe','no prob','any time','your quite welcome','sure thing','whatever you say boss','no worries man, I am glad to help','your welcome you ungrateful chameleon','ya. whatever.']
		speak(random.choice(responses),medium)
                return self.tree

        def __init__(self):
		tree = [[ Node( ['thank you','thanks'], self.thanks) ]]
                Command.__init__(self,tree)

