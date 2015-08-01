import commands

class CommandList:

	def __init__(self):
		self.list=[]
		self.initCommands()

	def getCommands(self):
		return self.list

	def initCommands(self):
		self.list.append(commands.null.Null())
		self.list.append(commands.stop.Stop())
		self.list.append(commands.weather.Weather())
		self.list.append(commands.telltime.TellTime())
		self.list.append(commands.goodnight.Goodnight())	
		self.list.append(commands.howareyou.HowAreYou())	
		self.list.append(commands.listalarms.ListAlarms())
		self.list.append(commands.listcommands.ListCommands())
		self.list.append(commands.lookup.LookUp())
		self.list.append(commands.playradio.PlayRadio())
		self.list.append(commands.thankyou.ThankYou())
		self.list.append(commands.remindme.RemindMe())
		self.list.append(commands.removealarm.RemoveAlarm())
		self.list.append(commands.why.Why())
		self.list.append(commands.sayhello.SayHello())
		self.list.append(commands.setalarm.SetAlarm())
		self.list.append(commands.stopradio.StopRadio())
		self.list.append(commands.party.Party())
		self.list.append(commands.themesong.ThemeSong())
		self.list.append(commands.adjustvolume.AdjustVolume())
		self.list.append(commands.nevermind.Nevermind())
		self.list.append(commands.nomatchfound.NoMatchFound())


if __name__=='__main__':
	print 'adding commands'
	list = CommandList()
