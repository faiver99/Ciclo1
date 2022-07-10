import os
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from tkinter import *
from tkinter import ttk
from sympy import symbols




def menu():
    os.system("clear")
    print("""
       Panel de Control 
           Los nodos y los elementos seran enumerados de izquierda a derecha y de arriba hacia abajo.

           1) Numero de lementos de la estructura sin contar resortes.
           1.1) Resortes.
           2) Mostrar valores de E,I,L,A de cada elemento.
           3) Matriz de Riguides de cada elemento en coordenadas globales.
           4) Indique la cargas externas para cada elemento.
           5) Fuerzas de empotramiento.
           7) Matriz de Riguides de toda la estructura.
           8) Deformaciones y momentos.
           9) Fuerzas internas.
           8) Salir. 


    """)

def minimenu():
    os.system("clear")
    print("""
       Cargas 
           1) Rectangular.
           2) Dos triangulos centrados.
           3) Triangular.
           4) Puntual.
           5) No tiene.
           
            
           """)



entrada = True
Elementos=0

while (entrada):

    menu()
    opc=float(input("Ingresa una Opcion: "))
   
    if opc==1:
        dato1="si"
        while dato1== "si":
            Elementos = int(input("Ingrese el numero de elmentos de su estructura:  "))
            lista=[]
            A=1
            while  A <= Elementos:
                Longitud = float(input(f"Ingrese la longitud del elemento  {A}: "))
                Inercia = float(input(f"Ingrese la Inercia del elemento {A}: "))
                ModuloE= float(input(f"Ingrese el valor de E del elemento {A}: "))
                THETA= float(input(f"Ingrese el valor de Theta θ (en grados) del elemento {A}: "))
                Area= float(input(f"Ingrese el valor del Area del elemento {A}: "))
                lista.append((Longitud,Inercia,ModuloE,THETA,Area)) ## tuplas
                A +=1 
                dato1="no"   
            
            print(f"El numero de elementos es:{Elementos} ")
            print(lista)

    if opc==1.1:
            cuantos=int(input("Ingrese cuantos resortes tiene su estructura: "))
            i=1
            while i<=cuantos:
                ingrese=int(input(f"En que nodo se encuentrael resorte {i}: "))
                k=int(input(f"Ingrese la costante k del resorte {i}: "))
                re=input("Ingrsa la orientacion del elemento vertical(1) o horizontal(2): " )

                i+=1
            
            
        
            
        

                
            
            # agenda[fecha]=lista
            # dato1=input("Ingrese otra fecha [si/no]:")
    
    if opc==2:
        if opc==2:


            ventana = Tk()
            ventana.geometry("1250x300")
            ventana.title("ANALISIS ESTRUCTURAL")


            arbol = ttk.Treeview(ventana,columns=("LONGITUD","MODULO E","INERCIA","THETA θ", "AREA"))

            k=1
            m=0
            
            for k in range (1,Elementos+1):
                
                arbol.insert("",END,text=f"{k}",values=(f"{lista[m][0]}",f"{lista[m][1]}",f"{lista[m][2]}",f"{lista[m][3]}",f"{lista[m][4]}"))
                k+=1
                m+=1
                    
            arbol.heading("#0",text="ELEMENTO")
            arbol.heading("LONGITUD",text="LONGITUD")
            arbol.heading("MODULO E",text="MODULO E")
            arbol.heading("INERCIA",text="INERCIA")
            arbol.heading("THETA θ",text="THETA θ")
            arbol.heading("AREA",text="AREA")
                
            arbol.place(x=10,y=10)
                              
            ventana.mainloop()  
     
    if opc==3:                                  
        i=1
        n=0
        
        matriz=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    
        for i in range(1,Elementos+1) :
            a = math.radians((lista[n][3]))
            landa=math.cos(a)
            b= math.radians((lista[n][3]))
            miu=math.cos(b)

             # PRIMERA FILA 
            A1=(((lista[n][4])*(lista[n][1]))/(lista[n][0]))*(landa**2)+((12*lista[n][1])*(lista[n][2])/((lista[n][0])**3))*miu**2
            A2=((((lista[n][4])*(lista[n][1]))/(lista[n][0]))-((12*lista[n][1])*(lista[n][2])/((lista[n][0])**3)))*landa*miu
            A3=((-6*(lista[n][1])*(lista[n][2]))/(lista[n][0]**2))*miu
            A4=-A1
            A5=-A2
            A6=-A3
            # SEGUNDA FILA 
            B1=A2
            B2=(((lista[n][4])*(lista[n][1]))/(lista[n][0]))*(miu**2)+((12*lista[n][1])*(lista[n][2])/((lista[n][0])**3))*(landa**2)
            B3=((6*(lista[n][1])*(lista[n][2]))/(lista[n][0]**2))*landa
            B4=-(A2)
            B5=-B2
            B6=B3
            # TERCERA FILA
            C1=A3
            C2=B3
            C3=(4*((lista[n][1])*(lista[n][2]))/(lista[n][0]))
            C4=((6*(lista[n][1])*(lista[n][2]))/(lista[n][0]**2))*miu
            C5=-B3
            C6=(2*((lista[n][1])*(lista[n][2]))/(lista[n][0]))
            # CUARTA FILA
            D1=-A1
            D2=-A2
            D3=C4
            D4=A1
            D5=A2
            D6=C4
            # QUINTA FILA 
            E1=-A2
            E2=B5
            E3=C5
            E4=A2
            E5=B2
            E6=C5
            # SEXTA FILA
            F1=-A3
            F2=B3
            F3=C6
            F4=-A3
            F5=-B3
            F6=C3
     
            # REDONDEOS          
            A1=round(A1, 5)
            A2=round(A2, 5)
            A3=round(A3, 5)
            A4=round(A4, 5)
            A5=round(A5, 5)
            A6=round(A6, 5)
            B1=round(B1, 5)
            B2=round(B2, 5)
            B3=round(B3, 5)
            B4=round(B4, 5)
            B5=round(B5, 5)
            B6=round(B6, 5)
            C1=round(C1, 5)
            C2=round(C2, 5)
            C3=round(C3, 5)
            C4=round(C4, 5)
            C5=round(C5, 5)
            C6=round(C6, 5)
            D1=round(D1, 5)
            D2=round(D2, 5)
            D3=round(D3, 5)
            D4=round(D4, 5)
            D5=round(D5, 5)
            D6=round(D6, 5)
            E1=round(E1, 5)
            E2=round(E2, 5)
            E3=round(E3, 5)
            E4=round(E4, 5)
            E5=round(E5, 5)
            E6=round(E6, 5)
            F1=round(F1, 5)
            F2=round(F2, 5)
            F3=round(F3, 5)
            F4=round(F4, 5)
            F5=round(F5, 5)
            F6=round(F6, 5)
   

            #FILA 1
            matriz[0][0]=A1
            matriz[0][1]=A2
            matriz[0][2]=A3
            matriz[0][3]=A4        
            matriz[0][4]=A5
            matriz[0][5]=A6
            #FILA 2
            matriz[1][0]=B1
            matriz[1][1]=B2
            matriz[1][2]=B3
            matriz[1][3]=B4
            matriz[1][4]=B5
            matriz[1][5]=B6
            #FILA 3
            matriz[2][0]=C1
            matriz[2][1]=C2
            matriz[2][2]=C3
            matriz[2][3]=C4
            matriz[2][4]=C5
            matriz[2][5]=C6
            #FILA 4
            matriz[3][0]=D1
            matriz[3][1]=D2
            matriz[3][2]=D3
            matriz[3][3]=D4
            matriz[3][4]=D5
            matriz[3][5]=D6
            #FILA 5
            matriz[4][0]=E1
            matriz[4][1]=E2
            matriz[4][2]=E3
            matriz[4][3]=E4
            matriz[4][4]=E5
            matriz[4][5]=E6
            #FILA 6 
            matriz[5][0]=F1
            matriz[5][1]=F2
            matriz[5][2]=F3
            matriz[5][3]=F4
            matriz[5][4]=F5
            matriz[5][5]=F6
            

            # MATRIZ = np.array(matriz)
            # print(matriz)
            
                         
            print(f"La matriz de rigidez del del elemento {i}")       
            for i in range(6):
                for j in range(6):
                    b=round(matriz[i][j], 2)
                    print (b, end="\t" )
                print(" ")

            # total= np.zeros((Elementos))    
            # total[n][i]= np.zeros((6,6))    
            

            # while i <= Elementos:

            #     total[n][i]=matriz     
                    
            i+=1
            n+=1  

            # print(total) 

    if opc==4:
        minimenu()

        print("Acontinuacion debera ingresar el tipo de la fuerza externa a la que esta sometido cada elemento") 
        i=1
        n=0
        p1=1
        p2=0
        c1=1
        c2=0
        matriz2= np.zeros((Elementos, 6))
        while i<= Elementos:
            
            tipo= int(input(f"Ingrese el tipo de carga para el elemento {i}: "))

            while tipo == 5 and i<=Elementos:
                tipo= input(f"Ingrese el tipo de carga parael elemento {i+1}: ")
                i+=1
                n+=1 
                p2+=1                    
               
            if tipo==1:
                
                carga=float(input("Ingrese la magnitud carga: "))
                m1=((carga)*(lista[n][0])**2)/(12)
                m2=-m1
                m1=round(m1, 2)      
                m2=round(m2, 2)
                matriz2[p2][2]=m1
                matriz2[p2][5]=-m1
                fy1=(carga*(lista[n][0])/2)
                fy2=fy1
                fy2=round(fy2, 2)
                fy1=round(fy1, 2)
                matriz2[p2][1]=fy1
                matriz2[p2][4]=fy2
                print(matriz2)
                i+=1
                n+=1 
                p2+=1 
                    

                
            if tipo==4:

                    carga=float(input("Ingrese la magnitud carga: "))

                    print("Teniendo en cuenta la ubicacion de la carga puntual sobre el elemento llamaremos 'a' a la distancia de izquierda a derecha desde el inicio del elemento hasta la carga y 'b' para la distacia de derecha a izquierda desde el fin del elemento hasta la carga" )

                    a=float(input("Ingrese a: "))
                    b=float(input("Ingrese b: "))
                    while a+b != lista[n][0]:
                        print(f"La sumade a+b={lista[n][0]}")
                        a=float(input("Ingrese a: "))
                        b=float(input("Ingrese b: "))


                    m1=((carga*(a)*(b**2))/(lista[n][0])**2)
                    m2=(-((carga)*(a**2)*(b))/(lista[n][0])**2)      
                    m1=round(m1, 2)      
                    m2=round(m2, 2)      
                    matriz2[p2][2]=m1
                    matriz2[p2][5]=m2
                    fy2=(-m1-m2+carga*a)/(lista[n][0])
                    fy1=-fy2+carga
                    fy2=round(fy2, 2)
                    fy1=round(fy1, 2)
                    matriz2[p2][1]=fy1
                    matriz2[p2][4]=fy2
                    print(matriz2)
                    i+=1
                    p2+=1
                    n+=1

            
            if tipo==3:
                lado=input("A que lado es mayor la altura del triangulo si es a la derecha ingresa D y si es a la izquierda IZ : ")


                if lado=="IZ":
                    carga=float(input("Ingrese la magnitud carga: "))  
                    m1=((carga)*(lista[n][0]**2))/(20)
                    m2=(-(carga)*(lista[n][0]**2))/(30)
                    m1=round(m1, 2)      
                    m2=round(m2, 2)
                    matriz2[p2][2]=m1
                    matriz2[p2][5]=m2
                    fy1=(lista[n][0]/20)*(7*carga)
                    fy2=(lista[n][0]/20)*(3*carga)
                    fy2=round(fy2, 2)
                    fy1=round(fy1, 2)
                    matriz2[p2][1]=fy1
                    matriz2[p2][4]=fy2
                    print(matriz2)
                    i+=1
                    p2+=1
                    n+=1

                if lado=="D":
                    carga=float(input("Ingrese la magnitud carga: "))  
                    m1=((carga)*(lista[n][0]**2))/(30)
                    m2=(-(carga)*(lista[n][0]**2))/(20)
                    m1=round(m1, 2)      
                    m2=round(m2, 2)
                    matriz2[p2][2]=m1
                    matriz2[p2][5]=m2
                    fy1=(lista[n][0]/20)*(3*carga)
                    fy2=(lista[n][0]/20)*(7*carga)
                    fy2=round(fy2, 2)
                    fy1=round(fy1, 2)
                    matriz2[p2][1]=fy1
                    matriz2[p2][4]=fy2
                    print(matriz2)
                    i+=1
                    p2+=1
                    n+=1


            if tipo==2 :
               carga=float(input("Ingrese la magnitud carga: "))  
               m1=(5*(carga)*(lista[n][0]**2))/(96)
               m2=(-5*(carga)*(lista[n][0]**2))/(96)
               m1=round(m1, 2)      
               m2=round(m2, 2)
               matriz2[p2][2]=m1
               matriz2[p2][5]=m2
               fy2=(lista[n][0]*carga)/4
               fy1=fy2
               fy2=round(fy2, 2)
               fy1=round(fy1, 2)
               matriz2[p2][1]=fy1
               matriz2[p2][4]=fy2
               print(matriz2)
               i+=1
               p2+=1
               n+=1

        print("Desea adicionar otra cargas a algun elementos")
        add=input("Si o No: ")       


        if add=="si":
                i=1
                n=0
                p1=1
                p2=0
                c1=1
                c2=0
                
                
                while i<= Elementos:
                    
                    minimenu()
                    tipo= int(input(f"Ingrese el tipo de carga a adicionar al elemento {i}: "))

                    if tipo==1:
                
                      carga=float(input("Ingrese la magnitud carga: "))
                      m1=((carga)*(lista[n][0])**2)/(12)
                      m2=-m1
                      m1=round(m1, 2)      
                      m2=round(m2, 2)
                      matriz2[p2][2]=matriz2[p2][2]+m1
                      matriz2[p2][5]=matriz2[p2][5]+(-m1)
                      fy1=(carga*lista[n][0])/2
                      fy2=fy1
                      fy2=round(fy2, 2)
                      fy1=round(fy1, 2)
                      matriz2[p2][1]=matriz2[p2][1]+fy1
                      matriz2[p2][4]=matriz2[p2][4]+fy2
                      print(matriz2) 
                      i+=1   
                      p2+=1 
                      n+=1
                      
                    
                    if tipo==4:



                        carga=float(input("Ingrese la magnitud carga: "))

                        print("Teniendo en cuenta la ubicacion de la carga puntual sobre el elemento llamaremos 'a' a la distancia de izquierda a derecha desde el inicio del elemento hasta la carga y 'b' para la distacia de derecha a izquierda desde el fin del elemento hasta la carga" )

                        a=float(input("Ingrese a: "))
                        b=float(input("Ingrese b: "))
                        while a+b != lista[n][0]:
                           print(f"La sumade a+b={lista[n][0]}")
                           a=float(input("Ingrese a: "))
                           b=float(input("Ingrese b: "))


                        m1=((carga*(a)*(b**2))/(lista[n][0])**2)
                        m2=(-((carga)*(a**2)*(b))/(lista[n][0])**2)      
                        m1=round(m1, 2)      
                        m2=round(m2, 2)      
                        matriz2[p2][2]=matriz2[p2][2]+m1
                        matriz2[p2][5]=matriz2[p2][5]+m2
                        fy2=(-m1-m2+carga*a)/(lista[n][0])
                        fy1=-fy2+carga
                        fy2=round(fy2, 2)
                        fy1=round(fy1, 2)
                        matriz2[p2][1]=matriz2[p2][1]+fy1
                        matriz2[p2][4]=matriz2[p2][4]+fy2
                        print(matriz2)
                        i+=1
                        p2+=1
                        n+=1
                           

                    if tipo==3:
                       lado=input("A que lado es mayor la altura del triangulo si es a la derecha ingresa D y si es a la izquierda IZ : ")


                       if lado=="IZ":
                           carga=float(input("Ingrese la magnitud carga: "))  
                           m1=((carga)*(lista[n][0]**2))/(20)
                           m2=(-(carga)*(lista[n][0]**2))/(30)
                           m1=round(m1, 2)      
                           m2=round(m2, 2)
                           matriz2[p2][2]=matriz2[p2][2]+m1
                           matriz2[p2][5]=matriz2[p2][5]+m2
                           fy1=(lista[n][0]/20)*(7*carga)
                           fy2=(lista[n][0]/20)*(3*carga)
                           fy2=round(fy2, 2)
                           fy1=round(fy1, 2)
                           matriz2[p2][1]=matriz2[p2][1]+fy1
                           matriz2[p2][4]=matriz2[p2][4]+fy2
                           print(matriz2)
                           i+=1
                           p2+=1
                           n+=1
                               
                        
                       if lado=="D":
                            carga=float(input("Ingrese la magnitud carga: "))  
                            m1=((carga)*(lista[n][0]**2))/(30)
                            m2=(-(carga)*(lista[n][0]**2))/(20)
                            m1=round(m1, 2)      
                            m2=round(m2, 2)
                            matriz2[p2][2]=matriz2[p2][2]+m1
                            matriz2[p2][5]=matriz2[p2][5]+m2
                            fy1=(lista[n][0]/20)*(3*carga)
                            fy2=(lista[n][0]/20)*(7*carga)
                            fy2=round(fy2, 2)
                            fy1=round(fy1, 2)
                            matriz2[p2][1]=matriz2[p2][1]+fy1
                            matriz2[p2][4]=matriz2[p2][4]+fy2
                            print(matriz2)
                            i+=1     
                            p2+=1
                            n+=1 
                             

                    if tipo==2 :
                      carga=float(input("Ingrese la magnitud carga: "))  
                      m1=(5*(carga)*(lista[n][0]**2))/(96)
                      m2=(-5*(carga)*(lista[n][0]**2))/(96)
                      m1=round(m1, 2)      
                      m2=round(m2, 2)
                      matriz2[p2][2]=matriz2[p2][2]+m1
                      matriz2[p2][5]=matriz2[p2][5]+m2
                      fy2=(lista[n][0]*carga)/4
                      fy1=fy2
                      fy2=round(fy2, 2)
                      fy1=round(fy1, 2)
                      matriz2[p2][1]=matriz2[p2][1]+fy1
                      matriz2[p2][4]=matriz2[p2][4]+fy2
                      print(matriz2)
                      i+=1     
                      p2+=1
                      n+=1


                    if tipo==5:
                        i+=1     
                        p2+=1
                        n+=1



        if add=="no":
            print("Exelente podemos continuar")           



        if tipo not in(1,2,3,4,5,6):
           print("Opcion incorrecta")  
        

        
        
    if opc==5:
            ventana = Tk()
            ventana.geometry("1350x300")
            ventana.title("ANALISIS ESTRUCTURAL")


            arbol = ttk.Treeview(ventana,columns=("FXI","FYI","MI","FXJ","FYJ","MJ"))

            k=1
            m=0
            
            for k in range (1,Elementos+1):
                
                arbol.insert("",END,text=f"{k}",values=(f"{matriz2[m][0]}",f"{matriz2[m][1]}",f"{matriz2[m][2]}",f"{matriz2[m][3]}",f"{matriz2[m][4]}",f"{matriz2[m][5]}"))
                k+=1
                m+=1
                    
            arbol.heading("#0",text="ELEMENTO")
            arbol.heading("FXI",text="FXI")
            arbol.heading("FYI",text="FYI")
            arbol.heading("MI",text="MI")
            arbol.heading("FXJ",text="FXJ")
            arbol.heading("FYJ",text="FYJ")
            arbol.heading("MJ",text="Mj")
                
            arbol.place(x=10,y=10)
                              
            ventana.mainloop()

       
    if opc==6: 
        i=1
        n=0
        for i in range(1,Elementos+1):
            print("Matriz de transformacion")
            trasn=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

            if lista[n][3]==0:
                n+=1
                i+=1


            
            if lista[n][3]!=0:

             #FILA 1
                trasn[0][0]= math.cos(math.radians(lista[n][3]))
                trasn[0][1]= math.sin(math.radians(lista[n][3]))
                trasn[0][2]=0
                trasn[0][3]=0        
                trasn[0][4]=0
                trasn[0][5]=0
            #FILA 2
                trasn[1][0]=-math.sin(math.radians(lista[n][3]))
                trasn[1][1]= math.cos(math.radians(lista[n][3]))
                trasn[1][2]=0
                trasn[1][3]=0
                trasn[1][4]=0
                trasn[1][5]=0
            #FILA 3
                trasn[2][0]=0
                trasn[2][1]=0
                trasn[2][2]=1
                trasn[2][3]=0
                trasn[2][4]=0
                trasn[2][5]=0
            #FILA 4
                trasn[3][0]=0
                trasn[3][1]=0
                trasn[3][2]=0
                trasn[3][3]=math.cos(math.radians(lista[n][3]))
                trasn[3][4]=math.sin(math.radians(lista[n][3]))
                trasn[3][5]=0
            #FILA 5
                trasn[4][0]=0
                trasn[4][1]=0
                trasn[4][2]=0
                trasn[4][3]=-math.sin(math.radians(lista[n][3]))
                trasn[4][4]= math.cos(math.radians(lista[n][3]))
                trasn[4][5]=0
                #FILA 6 
                trasn[5][0]=0
                trasn[5][1]=0
                trasn[5][2]=0
                trasn[5][3]=0
                trasn[5][4]=0
                trasn[5][5]=1
                
                print(f"La matriz de transformacion del del elemento {i}")       
                
                

                for k in range(6):
                    for j in range(6):
                        b=round(trasn[k][j], 2)
                        print (b, end="\t" )
                    print(" ")  


                
                def trasponer(trasn)  :
                        traspuesta=[]
                        for i in range(len(trasn[0])):
                            traspuesta.append([])
                            for j in range(len(trasn)):
                                traspuesta[i].append(trasn[j][i])
                        return traspuesta

                
                traspuesta=trasponer(trasn) 
              
                print(f"La matriz de transformacion traspuesta del elemento {i} es ")       
                for k in range(6):
                    for j in range(6):
                        b=round(traspuesta[k][j], 2)
                        print (b, end="\t" )
                    print(" ")  

                def multiplicacion(trasn,matriz2)    :
                    if len(trasn[0])==len(matriz2):
                        k1=[]
                        for i in range(len(trasn)):
                            k1.append([])
                            for j in range(len(matriz2[0])):
                                k1[i].append(0)

                        for i in range(len(trasn)):
                            for j in range(len(matriz2[0])):
                                for k in range(len(trasn[0])):

                                    k1[i][j]+= trasn[i][k]*matriz2[k][j]

                        return k1
                    
                k1=multiplicacion(trasn,matriz2) 

                def total(k1,traspuesta):

                    if len(k1[0])==len(traspuesta):
                        k2=[]
                        for i in range(len(k1)):
                            k2.append([])
                            for j in range(len(traspuesta[0])):
                                k2[i].append(0)

                        for i in range(len(k1)):
                            for j in range(len(traspuesta[0])):
                                for k in range(len(k1[0])):

                                    k2[i][j]+= k1[i][k]*traspuesta[k][j]
                        return k2

                k2=multiplicacion(trasn,matriz2) 

                print(f"La matriz de empotramieltos en coordenadas globlales del elemento {i} es: ")   

                print(k2)

               






                    

                i+=1
                n+=1







           
    
    if opc==7:
        entrada = False
        print("Te esperamos pronto")

    if opc not in(1,1.1,2,3,4,5,6,7):
         print("Opcion incorrecta")

    time.sleep(5)    
   

print("final de programa")   






