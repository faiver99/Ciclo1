## una ves se define una tupla no se puede modificar los datosç

tupla=(1,2,3,4,5,6,"a","fruta",True,[1,2,3])
tupla[-1][2]=5
print(tupla)
# del tupla

## recorrido de ruplas 

for i in tupla:
    print(i)
lista=list(tupla)
print (lista)