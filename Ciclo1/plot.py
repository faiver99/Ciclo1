from tkinter import *
from tkinter import ttk

from sympy import symbols

ventana = Tk()
ventana.geometry("1023x400")
ventana.title("ANALISIS ESTRUCTURAL")


arbol = ttk.Treeview(ventana,columns=("LONGITUD","MODULO E","INERCIA","THETA θ"))
arbol.insert("",END,text="1",values=("10","15","1000","150º"))
arbol.insert("",END,text="2",values=("12","7","1000","150º"))
arbol.insert("",END,text="3",values=  ("12","7","1000","150º"))
arbol.insert("",END,text="4",values=("12","7","1000","150º"))
arbol.heading("#0",text="ELEMENTO")
arbol.heading("LONGITUD",text="LONGITUD")
arbol.heading("MODULO E",text="MODULO E")
arbol.heading("INERCIA",text="INERCIA")
arbol.heading("THETA θ",text="THETA θ")
'''
menu1 = arbol.insert("",END,text="Menú 1")
menu2 = arbol.insert("",END,text="Menú 2")
arbol.insert(menu1,END,text="Elemento 1")
arbol.insert(menu1,END,text="Elemento 2")
arbol.insert(menu1,END,text="Elemento 3")
arbol.insert(menu2,END,text="Elemento 1")
'''
arbol.place(x=10,y=10)


ventana.mainloop()
