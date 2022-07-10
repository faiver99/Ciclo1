with open("numeros.txt","w") as numeros:
    numeros.write("estos son los numeros de 1 al 10\n")

    for i in range(10):
       numeros.write(F"el numero es: {i+1} \n")

       