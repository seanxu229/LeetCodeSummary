'''Understand the TreeNode type
if one of the tree is none, then return the other tree
build the root of the new tree
then for each child node, use mergeTrees again
'''
solution:
class Solution:
	def mergeTrees(self, t1, t2):
	"""
	:type t1: TreeNode
	:type t2: TreeNode
	:rtype: TreeNode
	"""
		if t1 is None:
			return t2
		if t2 is None:
			return t1
		root=t1.val+t2.val
		root=TreeNode(root)
		root.left=self.mergeTrees(t1.left,t2.left)
		root.right=self.mergeTrees(t1.right,t2.right)
		return root