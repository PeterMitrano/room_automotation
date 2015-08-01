from multiprocessing import Process,Queue
from commandList import CommandList
from threading import Thread
import processSTT
from rec import rec
from commands.speak import speak
from getSMS import getSMS


speak("initializing")

#I keep forgetting this line
commandList = CommandList()

#create queue to store awaiting command
recQ=Queue() #receives translations from rec.py
commandQ=Queue() #recieves commandList from node.py

#created seperate threads for listening for texts and voice
recThread = Process(target=rec,args=(recQ,))
smsThread = Process(target=getSMS,args=(recQ,))

commandL=[]
#a list of translations. each element follwed by a medium "rec" or "SMS"
translations=[]

#start
recThread.start()
#smsThread.start()

while True:
	while not recQ.empty():
		trans=recQ.get() #text translations
		medium=recQ.get() #indicated text / rec
		translations.append(trans)
		translations.append(medium)
		i,node=processSTT.process(translations,commandList.list)

		if node == commandList.list[1].tree[0][0]: #stop node
			speak("terminating all commands")
			for cmd in commandL:
				cmd.terminate()
		else:			
			cmdThread = Process(target=node.executeAsync,args=(i,translations[0],commandQ,medium))
			commandL.append(cmdThread)
			cmdThread.start()

		del translations[:]

	while commandQ.qsize()>1:
		i=commandQ.get()
		newTree=commandQ.get()
		print i,newTree
		#update tree
		#commandList.list[i].tree=newTree			
		print str(commandList.list[i]),'command just finished'
		

