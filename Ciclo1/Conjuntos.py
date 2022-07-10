conjunto= {1,2,3,4,5} 
conjunto1= {1,2,3,4,5}
print(conjunto1)
conjunto.add((1,2,34,5))
print(conjunto)
conjunto1.update([1,2,3,4,5,6,7,8,1,2,3])
conjunto2= set(conjunto1)  ## set elimina los duplicados de un conjunto
print(conjunto1)
print(conjunto2)
conjunto.remove(1)