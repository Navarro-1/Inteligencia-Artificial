import pandas as pd 
grafo=pd.read_excel('grafos.x1sx', sheet_name='Hoja1', index_col=0)
grafo=grafo.fillna(0)
grafo

def ba(grafo):
    V=list (grafo.keys())
    v1='a'
    