'''Notes: the tree tilt is the sum of all node tilt!!
for each node, tilt is the difference between two subtree total values
build a sum function to calculate the sum value'''

class Solution:
	def findTilt(self, root):
	"""
	:type root: TreeNode
	:rtype: int
	"""
	self.ans = 0
	def _sum(node):
		if not node:
		return 0
		left, right = _sum(node.left), _sum(node.right)
		self.ans += abs(left - right)
		return node.val + left + right
	_sum(root)
	return self.ans