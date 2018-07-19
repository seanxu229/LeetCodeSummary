def quick(alist,start,end):
	'''快速排序'''
	if start>end:
		return
	mid=alist[start]
	low=start
	high=end
	while low<high:
		while low<high and alist[high]>mid:
			high -= 1
		alist[low]=alist[high]
		while low<high and alist[low]<mid:
			low+=1
		alist[high]=alist[low]
	alist[low]=mid
	quick(alist,start,low-1)
	quick(alist,low+1,end)

alist[54,26,93,17,77,31,44,55,20]
quick(alist,0,len(alist)-1)
print (alist)