import numpy 


lista=[1,2,3,4,5,'hola',True]

lista.append('final') ## agrega al final de la lista la palabra 'final'
lista[0]=0 ## para cambiar el valor en la posicion []
print(lista)
print (lista[0])

del lista[1]  ## elimina el valor en la posicion []

lista.remove(True) ## elimina el elemento por su nombre

## metodo pop
x = lista.pop(4)  ## elimina el elemento en la posicion dada () y guarda el retorna el valor eliminado en la varible x

print(lista)
print(" el valor eliminado es:",x)  


## del lista (me elimina toda la lista)


# concatenacion de listas

lista1=["hola  "]
lista2=["mundo "]

print(lista1+lista2)
print(lista2+lista1)

print(lista1)
lista1 *= 5
print(lista1)

## recoriddo de listas 

l= []

for i in range(1,18):
    l.append(i**2)
    print(l)
    print(len(l))

for i in l:
    print(i,i**2,i**3, end="")



# Listas multi dimencionales 

lis =[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
print(" el valor de la posicion 3 de la lista 2 es: ",lis[1][3])

for i in lis:
    for j in i:
        print(j)



## indexado negativoç

list= [1,2,3,4,5,6,7,89,0,12]

print("el valor final es: ",list[-1]) ## imprime el ultimo valor de la lista
list.pop()
print("el nuevo valor final es: ", list[-1])


## slicig

lista3=[1,2,3,4,5,6,7,8,90,1,2,23,122]
print(" la lista completa es: ",lista3)
lista4= lista3[1:7:2]  ## incicio:final:incremento 
lista5= lista3[-7:-1:2]  ## incicio:final:incremento 
print("la lista recortada es: ",lista4)
print("la lista recortada es: ",lista5)