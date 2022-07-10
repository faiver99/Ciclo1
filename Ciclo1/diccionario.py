diccionario = {
    "Azul":"Blue",
    "Rojo":"Red",
    "Verde":"Green",
    "1" : [1,2,3,4]

}


diccionario["Amarrillo"]= "yellow" # añadir un elemento

diccionario["Azul"]="BLUE"  # cambiear un elemento 

del diccionario["Verde"]  # eliminar un elemeto con la clave


print(diccionario)
print(diccionario.get("lila", "no existe el color en el programa"))
print(diccionario.keys())  ## para mostrar todas las claves del diccionario
print(diccionario.values()) ## para mostrar los valores de las claves
print(diccionario.items()) ## muestra todos los valores del diccionario en tuplas
print(len(diccionario)) # para mostrar la cantidad de elementos en el diccionario
## diccionario.clear() # para limpiar un diccionario
print(diccionario)


for i in diccionario:
    print(f'{i} : {diccionario[i]}')

print(diccionario["1"][2])    

for i in diccionario:
    lista= diccionario[i]
    for i in lista:
        print(i)
