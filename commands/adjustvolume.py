from speak import speak
from rec import rec
from node import Node
import subprocess as sub
from command import Command

class AdjustVolume(Command):

        def ask(self,translations,medium):
		speak("what percent volume?",medium)
                return self.tree

	def adjust(self,translations,medium):
		for trans in translations:
			m=re.search("([0-9]+)[\s\t]*percent volume",trans)
			if m:
				v=int(m.group(1))
				print	"volume:",v
				sub.call("mpc volume "+v,shell=True)
				return self.tree
		speak("failed to parse volume percentage",medium)
                return self.tree


        def __init__(self):
		tree = [[ Node(['adjust volume'], self.ask) ],[ Node(['percent volume'],self.adjust) ]]
                Command.__init__(self,tree)

