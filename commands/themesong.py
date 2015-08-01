from command import Command
from node import Node
import subprocess as sub

class ThemeSong(Command):

        def playTheme(self,translations,medium):
		sub.call("aplay /home/pi/Room/Sherlock_theme.wav",shell=True)
                return self.tree

        def __init__(self):
		tree = [[ Node( ['theme song','theme intro','intro song'], self.playTheme) ]]
                Command.__init__(self,tree)

