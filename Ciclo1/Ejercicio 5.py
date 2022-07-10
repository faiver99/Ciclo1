# ejercicio 5

print("Ejercicio 5 \n")

primerNumero=int(input("ingrese el primer numero:" ));
segundoNumero=int(input("ingrese el segundo numero:" ));
tercerNumero=int(input("ingrese el tercero numero:" ));

Numeros=[primerNumero,segundoNumero,tercerNumero]

Menor=None
Mayor=None

for n in Numeros:
    if Menor==None and Mayor==None:
        Menor=n 
        Mayor=n
    else:
        if n<Menor:
            Menor=n
        if n>Mayor:
            Mayor=n

rango=Mayor-Menor
            
print("El rango es:", rango)          
print("El numero mayor es:" ,Mayor )  
print("El numero menor es:" ,Menor )  




# los numero que se encuentren en la lista seran desvinculados de los datos originales 

