import os
import time


agenda = {}  # diccionario
def menu():
    os.system("clear")
    print("""
       Agenda Electronica
           1) Carga de datos en la agenda.
           2) Listado completo de la agenda.
           3) Consulta de una fecha.
           4) Salir. 


    """)
    

entrada = True

while (entrada):

    menu()
    opc=int(input("Ingresa una Opcion: "))
   
    if opc == 1:
        dato1="si"
        while dato1== "si":
            fecha = input("Ingrese la fecha en formato dd/mm/aa:  ")
            dato2="si"
            lista=[]
            while dato2=="si":
                hora = input("Ingrese la hora de la actividad con formato hh:mm")
                actividad = input("Ingresa la descripcion de la actividad")
                lista.append((hora,actividad)) ## tuplas
                dato2= input("Ingrese otra actividad para misma fecha [si/no]:")
            
            
            agenda[fecha]=lista
            dato1=input("Ingrese otra fecha [si/no]:")

    if opc==2:

        if (len(agenda)>0):
            print("Listado completo de su agenda")

            for fecha in agenda:
                print(fecha,end="---")
                for hora,actividad in agenda[fecha]:
                    print(f"---{hora}|{actividad}")
                
        else:
            print("No hay actividades en la agenda")
       
    if opc == 3 :
        if (len(agenda)>0):
            fecha = input("Ingresa la fecha que desea consultar en formato dd/mm/aa: ")
            if fecha in agenda:
                print(f"Para la fecha:{fecha} tiene las siguientes actividades")
                for hora,actividad in agenda[fecha]:
                    print(f"---{hora}|{actividad}")
            else:
                print("No hay actividad en la agenda para la fecha conssultada")
        else:
            print("No hay actividades en la agenda:")
     
    if opc==4:
        entrada = False
        print("Te esperamos pronto")

    if opc not in(1,2,3,4):
        print("Opcion incorrecta")

    time.sleep(5)    


print("final de programa")    