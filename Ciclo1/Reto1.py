import random



b=30

Intentos=0

n= random.randint(0,b)
 
num=int(input("Ingrese un numero: ")) 

while num > n and num <= b or num < n and num >= 0:
    
    if num > n and num <= b :
          print("¡Ups! Te pasaste")
          Intentos += 1 
          num=int(input("Ingrese un numero: "))       


    if num < n and num >= 0 : 
         print("¡Ups! Estás por debajo")
         Intentos += 1
         num=int(input("Ingrese un numero: ")) 
         
    if num == n:
        
         Intentos += 1
         print(f"¡LO LOGRASTE! Usaste {Intentos} intentos") 


while  num < 0 or num > b:
    print("¡Te saliste del intervalo!")  # no cuente como intervalo
    num=int(input("Ingrese un numero: "))

    while num > n and num <= b or num < n and num >= 0:
    
        if num > n and num <= b :
             print("¡Ups! Te pasaste")
             Intentos += 1 
             num=int(input("Ingrese un numero: "))       


        if num < n and num >= 0 : 
            print("¡Ups! Estás por debajo")
            Intentos += 1
            num=int(input("Ingrese un numero: ")) 
         
        if num == n:
        
            Intentos += 1
            print(f"¡LO LOGRASTE! Usaste {Intentos} intentos") 
            break



               
            