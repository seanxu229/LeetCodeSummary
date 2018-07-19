
'''change to binary, use bin() first
change it to a list then we can compare two lists element one by one.
Note: for each list, first two elements are '0' and 'b'
as the two lists' length may not be the same, we should compare from the last element.
use for loop, from the last element to third element from start. (range(-1,-len(s)+1,-1)
note:-len(s)+1 is not included .
for the longer list, the longer part if it's not '0', then count++

'''
class Solution:
	def hammingDistance(self, x, y):
	"""
	:type x: int
	:type y: int
	:rtype: int
	"""
		x=list(bin(x))
		y=list(bin(y))
		count=0
		if len(x)==len(y):
			for i in range(len(x)):
				if x[i]!=y[i]:
					count+=1
		return count
		if len(x)>len(y):
			x,y=y,x
		for i in range(-1,-len(x)+1,-1):
			if x[i]!=y[i]:
				count+=1
		for j in range(-len(x)+1,-len(y)+1,-1):
			if y[j]!='0':
				count+=1
		return count