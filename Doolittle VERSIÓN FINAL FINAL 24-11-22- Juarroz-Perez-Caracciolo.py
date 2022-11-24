#Dolittleversiónfinalfinal-Juarroz-Perez-Caracciolo- noviembre 2022-Computación- Profesores: Quinteros y Zapata
from http.client import OK
from ast import If
from re import L, U
import numpy as np 
#import math
def crear_matriz (fil,col):
    f = -1 ; c=-1
    e_fil=[]
    for f in range (fil):
        e_col= []
        f +=1
        for c in range (col):
            c +=1
            valor =(input("Introduzca el componente(%g, %g): "%(f,c)))
            e_col.append (valor)
        e_fil.append (e_col)
        matrizcoeficioentes = np.array (e_fil, float)
    print(matrizcoeficioentes)
    return matrizcoeficioentes
    


def crear_matrizTI (fil,col):
    print ("Ingrese la matriz resultados")
    f = -1 ; c=-1 
    e_fil=[]
    for f in range (fil):
        e_col= []
        f +=1
        for c in range (col):
            c +=1
            valor =(input("Introduzca los términos independientes(%g, %g): "%(f,c))) 
            e_col.append (valor)
        e_fil.append (e_col)
        matrizTI = np.array (e_fil, float)
    print(matrizTI)
    return matrizTI
fil = int(input("Introduzca el número de filas: "))
col = int(input("Introduzca el número de columnas: "))
if col == fil:
    matriz = crear_matriz (fil,col)
    resultados = crear_matrizTI (fil,1)
else:
    print ("La matriz debe ser cuadrada, reinicie el programa nuevamente")
    

def LU_doolittle(a):
    n = len (a)
    L = np.zeros([n,n])
    U = np.zeros([n,n])
    for i in range (n):
        L[i][i] = 1
        if i == 0:
            U[0][0] = a[0][0]
            for j in range (1,n):
                U[0][j] = a[0][j]
                L[j][0] = a[j][0]/U[0][0]
        else:
                for j in range (i,n): 
                    sumatoria = 0
                    for k in range (0,i):
                        sumatoria = sumatoria + L [i][k] * U [k][j]
                    U[i][j] = a[i][j] - sumatoria
                    for j in range (i + 1,n): 
                        sumatoria = 0   
                        for k in range (0,i):  
                            sumatoria = sumatoria + L[j][k] * U[k][i]
                        L[j][i] = (a[j][i] - sumatoria)/U[i][i]
    return L,U


det= np.linalg.det (matriz)

if det == 0:
    print ("El sistema no tiene solución")  
else:
    print("El determinante de la matriz de coeficiente es: ", det)    
    a = matriz
    b = resultados
    L,U = LU_doolittle(a)
    y = np.linalg.solve(L,b)
    x = np.linalg.solve(U,y)
    print("L:", L)
    print("U:", U)
    print('Sol',x)



