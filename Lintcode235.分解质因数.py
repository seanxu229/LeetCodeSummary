'''
分解质因数
'''
res=[]
while num!=1:
	for i in range(2,int(num+1)):
		if num%i==0:
			res.append(i)
			num=num//i
			break

f=2
while f*f<=num:
	while not n%f:
		res.append(f)
		num=num//f
	f=f+1
	if num>1:
		res.append(num)
