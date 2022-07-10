import tkinter
from tkinter import *
from tkinter import ttk
import math
import numpy

ventana=tkinter.Tk()
ventana.geometry("1000x600")
ventana.title("ANALISIS ESTRUCTURAL")

# etiqueta = tkinter.Label(ventana, text = " Matrices de Riguides de cada elemento en coordenada globales", bg="yellow")
# by = tkinter.Label(ventana, text = "Creado Por Faiver Vargas.")
# etiqueta.pack(side=tkinter.TOP , fill = tkinter.X)
# by.pack(side = tkinter.BOTTOM)
# by.pack(fill = tkinter.X)



Elementos= 3

matriz = [[1,2,3],
          [1,2,3],
          [1,2,3]] 


b=""  
for i in range(1,Elementos+1):

    fil=1
    col=0
    print("La matriz de rigidez del del elemento 1")       
    for i in range(3):
       for j in range(3):
           b+=str(matriz[i][j])+ '\t'   
       print(b)
       b =""      




    a1= tkinter.Label(ventana, text=("") )
    a1.grid(row=0, column=0)
    


    

   

    fil=fil+1
    col=col+1


ventana.mainloop()