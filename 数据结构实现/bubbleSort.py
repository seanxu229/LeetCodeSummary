'''bubble_sort implement'''
#version1
def bubble_sort1(alist):
	n=len(alist)
	for j in range(n-1):
		count=0
		for i in range(0,n-1-j):
			if alist[i]>alist[i+1]
				alist[i],alist[i+1]=alist[i+1],alist[i]
				count+=1
		if count==0:
			return alist
#加count可以试已经有序后及时跳出，降低算法复杂度

#version2
def bubble_sort2(alist):
	n=len(alist)
	for j in range(n-1,0,-1):
		for i in range(0,j):
			if alist[i]>alist[i+1]
				alist[i],alist[i+1]=alist[i+1],alist[i]