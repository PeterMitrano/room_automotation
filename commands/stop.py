#stops all currentlly executing commands
from command import Command
from node import Node
from speak import speak

class Stop(Command):

	def stop(self,translations,medium):
		#stop most recent commands
		#somehow have access to the command queue
		return self.tree

	def __init__(self):
		base= Node(['Stop','Shut up'],self.stop)
		tree=[[base]]
		Command.__init__(self,tree)
