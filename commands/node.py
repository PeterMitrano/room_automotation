class Node():

	def __init__(self,keys,func):
		#options/choices
		self.keys=keys
		self.confidence=0
		self.open=False
		self.func = func

	def openNode(self):
		self.open=True

	def closeNode(self):
		self.open=False

	def isOpen(self):
		return self.open

	def execute(self,translations):
		self.func(translations)

	def executeAsync(self,i,translations,queue,medium):
		newTree=self.func(translations,medium)
		queue.put(i)
		queue.put("FILLER PUT")
		#queue.put(newTree) #not pickleable. send extracted bool struct

	def __str__(self):
		try:
			return self.keys[0]+" node"
		except:
			return 'null'+" node"

	@staticmethod
	def closeAll(tree):
		for nodeLevelId in range(1,len(tree)): #dont close first level ones
			nodeLevel=tree[nodeLevelId]
			for node in nodeLevel:
				node.closeNode()
