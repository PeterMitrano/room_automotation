from command import Command
import subprocess as sub
from node import Node

class StopRadio(Command):

        def stop(self,translations,medium):
		sub.call('mpc stop',shell=True)
                return self.tree

        def __init__(self):
		tree = [[ Node( [ 'stop radio','stop music'], self.stop) ]]
                Command.__init__(self,tree)



if __name__ == '__main__':
	s = StopRadio()
