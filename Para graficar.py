>>> def burbuja(A):
	cnt=0
	for i in range(1,len(A)):
		for j in range(0,len(A)-1):
			cnt+=1
			if(A[j+1]<A[j]):
				aux=A[j]
				A[j]=A[j+1]
				A[j+1]=aux
	return cnt

>>> def selection(arr): 
 	cnt=0 
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
 	return cnt

>>> def quicksort(arr):
	cnt=0
	if len(arr)<=1:
		return arr
	piv=arr[0]
	izq=[]
	der=[]
	for i in range(1,len(arr)):
		cnt+=1
		if(arr[i]<piv):
			izq.append(arr[i])
		else:
			der.append(arr[i])
	return cnt

>>> def ord_insercion(arr):
	cnt=0
	for indice in range(1,len(arr)):
		valor=arrr[indice]
		i=indice-1
		cnt+=1
		while i>=0:
			if valor<arr[i]:
				arr[i+1]=arr[i]
				arr[i]=valor
				i=i-1
			else:
				break
	return cnt

>>> def rndar(lon):
	arr = []
	for r in range(lon):
		arr.append(random.randint(0, lon))
		return arr 