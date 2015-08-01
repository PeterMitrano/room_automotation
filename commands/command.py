class Command:

	def __init__(self,tree):
		self.tree=tree
		for node in self.tree[0]:
			node.openNode()
		self.confidence=0
		self.transcript=""

	def __str__(self):
		if len(self.tree[0][0].keys)>1:
			return self.tree[0][0].keys[0]+" command"
		return "null command"
	
