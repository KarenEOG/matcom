def minimo(arr):
	w=0
	k=arr[0]
	for w in arr:
		if(w<k):
		   k=w
		return k

	
 def ordenar(arr):
	arrsort=[]
	for k in range(len(arr)):
		w=minimo(arr)
		arr.remove(w)
		arr.sort.append(w)
	return arrsort