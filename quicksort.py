cnt=0
def quicksort(arr):
	global cnt
	if len(arr)<=1:
		return arr
	piv=arr[0]
	izq=[]
	der=[]
	for i in range(1,len(arr)):
		if(arr[i]<piv):
			izq.append(arr[i])
		else:
			der.append(arr[i])
		cnt+=1
	return quicksort(izq)+[piv]+quicksort(der)
