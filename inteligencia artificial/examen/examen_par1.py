import pandas as pd
import numpy as np
 
grafo=pd.read_excel(r'C:\Users\javro\OneDrive\Escritorio\ceti colomos\6to semestre\inteligencia artificial\examen\exa.xlsx',index_col=0)
grafo = grafo.fillna(np.inf)
 
V = list(grafo.columns)
n = len(V)
s = 0  
vertice=V.copy()
w = grafo.copy()
def prim(w,n,s,vertice):
 
 
    # V(i)=1 si el vértice se agrega al aem
    # V(i)=0 si el vértice no se agrega al aem
    for i in range(n):
        vertice[i]=0
 
    #Se agrega el vertice a: aem
    vertice[s] = 1
 
    # se comienza con un conjunto de aristas vacio
    E = []
 
    # Se ponen n-1 aristas en el aem
    for _ in range(n - 1):
        min = np.inf
        u, v = -1, -1
 
        #Se agrega la arista de peso minimo con un vertice
        #en el aem y un vertice que no este en el aem
        for i in range(n):
            if vertice[i]:
                for j in range(n):
                    if not vertice[j] and w.iloc[i, j] < min:
                        min = w.iloc[i, j]
                        u, v = i, j
 
        # Se pone el vertice y la arista en el aem
        if u != -1 and v != -1:
            vertice[v] = 1
            E.append((u, v, min))
    return E
 
 
E=prim(w,n,s,vertice)
Q = 0
print("Las aristas en el aem son:")
for a in E:
    print(f"({V[a[0]]},{V[a[1]]}) tiene un peso de {a[2]}")
    Q += a[2]
print(f"Con un peso total de {Q}")