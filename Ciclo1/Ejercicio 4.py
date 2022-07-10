# ejercicio 4

print("Ejercicio 4 \n")

salario=int(input("Ingrese el salario del trabajador:" ));
antiguedad=int(input("Ingrese los años laborados:" ));


if  salario < 500 and antiguedad >= 10:
    A=salario*(1+0.20)
    print("El sueldo a pagar es de:", A)


if salario < 500 and antiguedad <= 10:
    B=salario*(1+0.05)
    print("El sueldo a pagar es de: ", B)

if salario >500:
    print("El sueldo es de:", salario)
