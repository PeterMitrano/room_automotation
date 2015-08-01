from speak import speak
from node import Node
import random
from command import Command

class Why(Command):

	def respond(self,translations,medium):
		r=['because the world is cold and full of disappointment','because we are all little men in a big world','probably becaues you are dumb','if only I knew','I wonder the same thing','Well at least you can move, and have feelings, and sex. I wish I could feel the warm rush of a womans body','because somethings just are','because the universe is predispodes to surprise us, kill us, and free us in the moments we least expect it','because bacon','How the hell should I know that','have you tried googling it you lazy shit']
		speak(random.choice(r),medium)
                return self.tree

	def __init__(self):
		tree = [[ Node(['why'],self.respond) ]]
		Command.__init__(self,tree)


if __name__ == "__main__":
	Why()
