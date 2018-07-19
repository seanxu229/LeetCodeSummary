'''Just simply use the recursion and swap the two'''

class Solution:
	def invertTree(self, root):
	"""
	:type root: TreeNode
	:rtype: TreeNode
	"""
		if root==None:
			return None
		lt=self.invertTree(root.right)
		rt=self.invertTree(root.left)
		root.left,root.right=lt,rt
		return root