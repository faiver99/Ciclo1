matriz = [[1,2,3],
          [1,2,3],
          [1,2,3]] 
b=""  
print("La matriz de rigidez del del elemento 1")       
for i in range(3):
    for j in range(3):
        ##print((matriz[i][j]));
        b+=str(matriz[i][j])+ '\t'   
    print(b)
    b =""
    
    
   
