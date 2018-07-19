
'''check the null tree
check the root node
use the same function for 2 child node
Mysolytion:
'''
class Solution:
	def trimBST(self, root, L, R):
	"""
	:type root: TreeNode
	:type L: int
	:type R: int
	:rtype: TreeNode
	"""
		if not root:
			return None
		if root.val<L:
			return self.trimBST(root.right,L,R)
		if root.val>R:
			return self.trimBST(root.left,L,R)
		root.left=self.trimBST(root.left,L,R)
		root.right=self.trimBST(root.right,L,R)
		return root