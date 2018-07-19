'''前提是排好序了，有序的顺序表，必须相邻，即顺序表，不能是链条'''
def binary_search(alist,item):
	n=len(alist)
	if n>0:
		mid=n/2
		if alist[mid]==item:
			return True
		elif item<alist[mid]:
			binary_search(alist[:mid],item)
		else:
			binary_search(alist[mid+1:],item)
	return False

def binary_search1():
	#not recursion
	n=len(alist)
	first=0
	last=n-1
	while first<=last:
		mid=(first+last)//2
		if alist[mid]==item:
			return True
		elif alist[mid]<item:
			first=mid+1
		else:
			last=mid-1
	return False