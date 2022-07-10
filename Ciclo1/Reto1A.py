intentos=0

      while n <= b:
           num=int(input("Ingrese un numero"))
           intentos+=1
           if num >n and num <=b:
               print("¡Ups! Te pasaste")
           elif num <n and num>=0:
                print("¡Ups! Estás por debajo")
           elif num < 0 or num>b: 
               print("¡Te saliste del intervalo!")
               intentos -=1
           else :
               print(f"¡LO LOGRASTE! Usaste {intentos} intentos") 
               break
            
