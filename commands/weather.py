import re
from command import Command
from rec import rec
from speak import speak
from node import Node
from feedparser import parse

class Weather(Command):

	def base(self,translations,medium):
		feed = parse("http://weather.yahooapis.com/forecastrss?w=2506736")
		weather = feed['entries'][0]['summary_detail']['value']
		self.lines = weather.split('\n')
		print self.lines
		report = self.lines[2][:-6]
		report=re.sub(' F',' Fahrenheit',report)
		speak("the current weather is. "+report+". Do you want to hear the rest of the week?",medium)
		self.tree[1][0].openNode() #yes
		self.tree[1][1].openNode() #no
		return self.tree
		
	#when you respond 
	def affirmFull(self,translations,medium):
  		for i in range(4,len(self.lines)-2):
			report = self.lines[i][:-6]
			report=re.sub('Sun ','Sunday ',report)
			report=re.sub('Mon ','Monday ',report)
			report=re.sub('Tue ','Tuesday ',report)
			report=re.sub('Wed ','Wednesday ',report)
			report=re.sub('Thu ','Thursday ',report)
			report=re.sub('Fri ','Friday ',report)
			report=re.sub('Sat ','Saturday ',report)
			speak(report,medium)
		Node.closeAll(self.tree)
		return self.tree

	def daffirmFull(self,translations,medium):
		speak("ok then",medium)
		Node.closeAll(self.tree)
		return self.tree

	def __init__(self):
		tree=[] #this command needs two levels, base and a yes/no
		base=Node(['weather','forecast'],self.base)
		affirmFull=Node(['yes','ok'],self.affirmFull)
		daffirmFull=Node(['no'],self.daffirmFull)
		tree=[[base],[affirmFull,daffirmFull]]
		Command.__init__(self,tree)

if __name__ == '__main__':
	w = Weather()

