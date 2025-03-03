import pandas as pd

grafos=pd.read_excel(r'C:\Users\javro\OneDrive\Escritorio\ceti colomos\6to semestre\inteligencia artificial\act2_grafos\grafos.xlsx',sheet_name='grafo1',index_col=0)
grafos=grafos. fillna(0)

def be(V, E):
    Vp = {V[0]}
    Ep = []
    w = V[0] #"a"

    while True:
        while True:
            arista_minima = None
            for vK in V:
                if vK in Vp:
                    continue
                if grafos. loc[w, vK] > 0:
                    if not arista_minima or grafos. loc[w, vK] < grafos. loc [arista_minima[0], arista_minima[1]]:
                        arista_minima = (w, vK)

            if arista_minima: 
                w, vK = arista_minima
                Ep. append ((w, vK))
                Vp. add(vK)
                w = vK
            else:
                break
        if w == V[0]:
            return Ep, Vp
        for u, v in Ep[::-1]:
            if v == w:
                w = u
                break
V=list(grafos. keys())
E = []
arbol_expansion = be(V, E)

print("Aristas del árbol de expansión:", arbol_expansion[0])
print("Vértices del árbol de expansión:", arbol_expansion[1])