from command import Command
from node import Node

class Null(Command):
	
	def null(self,translations,medium):
		return self.tree

	def __init__(self):
		tree = [[ Node( [], self.null) ]]
		Command.__init__(self,tree)
