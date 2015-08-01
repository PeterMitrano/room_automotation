from speak import speak
from node import Node
from command import Command
import random

class HowAreYou(Command):

        def respond1(self,translations,medium):
		statuses=['I am doing ok','pretty good','not bad','freaking awesome','a little hungover','I am feeling a bit sassy today','alright, I guess','great','good','horrible','incomplete. whos fault is that I wonder','terrific. just peachy','good, good','lonely','tired']
		questions=['and you?','and your self','what about you?','how are you?']
		speak(random.choice(statuses)+" . "+random.choice(questions),medium)
		self.tree[1][0].openNode()
                return self.tree

	def respond2(self,translations,medium):
		for trans in translations:
			if "good" in trans:
				speak("well Ia m glad you are doing so well",medium)
			elif "bad" in trans:
				speak("awwww, I am so sorry to hear that. feel better soon",medium)
			else:
				speak("yes, I understand. talk to you later Watson",medium)
		Node.closeAll(self.tree)
                return self.tree

        def __init__(self):
		base = Node(['how are you','what is up'],self.respond1)
		userResponse = Node(['I am',"I'm"],self.respond2)
		tree=[[base] , [userResponse]]
                Command.__init__(self,tree)
