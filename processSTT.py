from fuzzywuzzy import fuzz

#returns a node NOT a command
def process(translations,cmdList):

	print 'translations',translations[0]

	bestNode=cmdList[len(cmdList)-1].tree[0][0] #no match found command
	bestNode.confidence=40

	for translation in translations[0]: #1-4
		for cmd in cmdList:	#10-20
			for nodeListId in range(len(cmd.tree)):
				if nodeListId>0 or "Sherlock" in translation:
					nodeList=cmd.tree[nodeListId]
					for node in nodeList: #2-6
						if node.isOpen():
							for key in node.keys: #1-4
								confidence = fuzz.token_set_ratio(key,translation)
								if confidence>bestNode.confidence:
									bestNode.keys=node.keys
									bestNode.open=node.open
									bestNode.func=node.func
									if confidence > 60:
											print "Executing:",node.keys
											return cmdList.index(cmd),node
											#return node
	print "null command"
	return 0,cmdList[0].tree[0][0]
	#return cmdList[0].tree[0][0]
