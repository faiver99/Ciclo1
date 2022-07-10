import math
import numpy as np
import pandas 




i=1
n=0
Elementos=3
matriz=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
lista=[[1,2,3,45],[5,6,7,8],[12,23,22,11]]
while i <= Elementos:

    a = math.radians((lista[n][3]))
    landa=math.cos(a)
    b= math.radians((lista[n][3]))
    miu=math.cos(b)
    # PRIMERA FILA 
    A1=(((lista[n][1])*(lista[n][2]))/(lista[n][0]))*(landa**2)+((12*lista[n][1])*(lista[n][2])/((lista[n][0])**3))*miu**2
    A2=((((lista[n][1])*(lista[n][2]))/(lista[n][0]))-((12*lista[n][1])*(lista[n][2])/((lista[n][0])**3)))*landa*miu
    A3=((-6*(lista[n][1])*(lista[n][2]))/(lista[n][0]**2))*miu
    A4=-A1
    A5=-A2
    A6=-A3
    # SEGUNDA FILA 
    B1=A2
    B2=(((lista[n][1])*(lista[n][2]))/(lista[n][0]))*(miu**2)+((12*lista[n][1])*(lista[n][2])/((lista[n][0])**3))*(landa**2)
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
    F1=A3
    F2=B3
    F3=C6
    F4=-A3
    F5=-B3
    F6=C3
     
    # REDONDEOS  
    A1=round(A1, 2)
    A2=round(A2, 2)
    A3=round(A3, 2)
    A4=round(A4, 2)
    A5=round(A5, 2)
    A6=round(A6, 2)
    B1=round(B1, 2)
    B2=round(B2, 2)
    B3=round(B3, 2)
    B4=round(B4, 2)
    B5=round(B5, 2)
    B6=round(B6, 2)
    C1=round(C1, 2)
    C2=round(C2, 2)
    C3=round(C3, 2)
    C4=round(C4, 2)
    C5=round(C5, 2)
    C6=round(C6, 2)
    D1=round(D1, 2)
    D2=round(D2, 2)
    D3=round(D3, 2)
    D4=round(D4, 2)
    D5=round(D5, 2)
    D6=round(D6, 2)
    E1=round(E1, 2)
    E2=round(E2, 2)
    E3=round(E3, 2)
    E4=round(E4, 2)
    E5=round(E5, 2)
    E6=round(E6, 2)
    F1=round(F1, 2)
    F2=round(F2, 2)
    F3=round(F3, 2)
    F4=round(F4, 2)
    F5=round(F5, 2)
    F6=round(F6, 2)
   

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





   
    










    #         arbol.heading("LONGITUD",text="LONGITUD")
    #         arbol.heading("MODULO E",text="MODULO E")
    #         arbol.heading("INERCIA",text="INERCIA")
    #         arbol.heading("THETA θ",text="THETA θ")

          
        
    i+=1
    n+=1
   
    import numpy as np

    MATRIZ = np.array(matriz)

    for line in MATRIZ:
        print ('  '.join(map(str, line)))
        # ¡print(landa, miu,A1,A2,A3,A4,A5,A6)

