import subprocess as sub
from node import Node
from command import Command

class PlayRadio(Command):

        def play(self,translations,medium):
		sub.call('mpc play',shell=True)
                return self.tree

        def __init__(self):
		tree = [[ Node( ['play radio'], self.play) ]]
                Command.__init__(self,tree)

