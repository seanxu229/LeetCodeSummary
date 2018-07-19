class Node(object):
	"""docstring for Node"""
	def __init__(self, item):
		self.elem=item
		self.lchild=lchild
		self.rchild=rchild
class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root=root

	def add(self,elem):
		node=Node(elem)
		if self.root==None:
			self.root=node
		else:
			queue=[]
			queue.append(self.root)
			while queue:
				cur=queue.pop(0)
				if cur.lchild==None:
					cur.lchild=node
					return
				elif cur.rchild=None:
					cur.rchild=node
					return
				else:
					queue.append(cur.lchild)
					queue.append(cur.rchild)
	def breadth_travel(self):
		if root==None:
			return
		queue=[]
		queue.append(root)
		while queue:
			node=queue.pop(0)
			print node.elem,
			if node.lchild!=None:
				queue.append(node.lchild)
			if node.rchild!=None:
				queue.append(node.rchild)