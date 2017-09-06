cnt=0
def selection(arr):
	global cnt
	for i in range(0,len(arr)-1):
		val=1
		for j in range(i+1,len(arr)):
			cnt+=1
			if arr[j]<arr[val]:
			  val=j
		if val !=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr


import random

def ran_n(n,lim_i=0,lim_s=100):
	arr=[]
	for i in range(n):
		arr.append(random.randit(lim_i,lim_s))
	return arr