from tkinter import *
from tkinter import messagebox

class Ventana:

	def __init__(self,inter):
		self.interfaz = inter
		self.interfaz.geometry("500x500")
		self.interfaz.title("Analisis Estructural")
		self.num1 = IntVar()
		self.num2 = IntVar()
        
		self.dibujarVentana()

	def dibujarVentana(self):
		Label(self.interfaz,text="Cuantos elementos hay en su estructura: ").place(x=10,y=10)
		Entry(self.interfaz,textvariable=self.num1).place(x=20,y=30)
		
		Button(self.interfaz,command=self.sumar,text="Sumar").place(x=50,y=110)

	def sumar(self): 
               
		# res = self.num1.get()
		messagebox.showinfo("Continuar",)

  
obj = Ventana(Tk())
obj.interfaz.mainloop()