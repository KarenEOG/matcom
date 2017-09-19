cnt=0
def orden_por_insercion(array):
	global cnt
	for indice in range(1,len(array)):
		valor=array[indice] #Valor es el elemento que vamos a comparar
		i=indice-1		#i es el avlor anterior al alemento
		while i>=0:
			cnt+=1
 			if valor<array[i]: #comparamos valor con el elemento anterior
				array[i+1]=array[i]  #intercambiamos los valores
				array[i]=valor
				i-=1  #Decrementamos en 1el valor de 1
			else:
 				break
	return array,cnt 
