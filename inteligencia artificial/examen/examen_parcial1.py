import pandas as pd
import numpy as np
 
grafo=pd.read_excel(r'C:\Users\javro\OneDrive\Escritorio\ceti colomos\6to semestre\inteligencia artificial\examen\exa.xlsx',index_col=0)
grafo=grafo.fillna(0)
grafo
 
def prim(grafo,n,s):
    u = [0] * n
    u[s] = 1
    aem = []
   
    for i in range(1,n):
        min= np.inf
        vertice = -1
        e = (-1,-1)
        for j in range(n):
            if (u[j] == 1):
                for k in range(n):
                    if u[k] == 0 and grafo.iloc[j][k] < min:
                        vertice = k
                        e = [j,k]
                        min = grafo.iloc[j][k]
        aem.append(e)
        u[vertice] = 1
    return aem  
 
s = 0
n = len(grafo)
 
print(prim(grafo,n,s))