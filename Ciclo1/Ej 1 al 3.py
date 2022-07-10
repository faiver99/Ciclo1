
# ejercicio 1 
print("Ejercicio 1 \n")

primerNumero=int(input("ingrese el primer numero:" ));
segundoNumero=int(input("ingrese el segundo numero:" ));
tercerNumero=int(input("ingrese el tercero numero:" ));


if primerNumero > 10 and segundoNumero > 10 and  tercerNumero > 10: 
    print("Todos los numeros ingresados son mayores a 10")
else:
 print("Alguno(s) de los numeros ingresados no es mayor a 10 \n" )


# ejercicio 2

print("Ejercicio 2 \n")
primerNumero=int(input("ingrese el primer numero:" ));
segundoNumero=int(input("ingrese el segundo numero:" ));
tercerNumero=int(input("ingrese el tercero numero:" ));


if primerNumero > 10 or segundoNumero > 10 or  tercerNumero > 10: 
    print("Alguno(s) de los numeros ingresados (es/son) mayores a 10 ")
else:
 print("Ninguno de los numeros ingresados es mayor a 10 \n")


# ejercicio 3

print("Ejercicio 3 \n")

primerNumero=int(input("ingrese el primer numero:" ));
segundoNumero=int(input("ingrese el segundo numero:" ));
tercerNumero=int(input("ingrese el tercero numero:" ));

if primerNumero == segundoNumero == tercerNumero :
    A=int(primerNumero+segundoNumero)
    print("La Suma del primero y segundo es:", A)
    B=tercerNumero*A
    print("la multiplicacion de los numeros sumados por el tercer numero es :", B)
else:
  print(" los numeros ingresados no son iguales \n")


# ejercicio 4

print("Ejercicio 4 \n")

salario=int(input("Ingrese el salario del trabajador:" ));
antiguedad=int(input("Ingrese los años laborados:" ));


if  salario < 500 and antiguedad >= 10:
    A=500*(1+0.20)
    print("El sueldo a pagar es de:", A)


if salario < 500 and antiguedad <= 10:
    B=500*(1+0.05)
    print("El sueldo a pagar es de:", B)

if salario >500:
    print("El sueldo es de:", salario)




