def conflicto(fila, k):
    for i in range(1, k):
        if fila[i] == fila[k] or abs(fila[i] - fila[k]) == abs(i - k):
            return True
    return False

def cuatro_reinas():
    fila = [0] * 5  
    k = 1  
    fila[k] = 0  

    while k > 0:
        fila[k] += 1  
        print(f"Intentando colocar reina en columna {k}, fila {fila[k]}")

        while fila[k] <= 4 and conflicto(fila, k):  
            print(f"Conflicto en columna {k}, fila {fila[k]}. Probando siguiente fila...")
            fila[k] += 1
        
        if fila[k] <= 4:
            if k == 4:  #
                print("¡Se encontró una solución!")
                for col in range(1, 5):
                    print(f"Reina en columna {col}, fila {fila[col]}")
                return True  
            else:
                print(f"Reina colocada en columna {k}, fila {fila[k]}. Avanzando a la siguiente columna...")
                k += 1  
                fila[k] = 0  
        else:
            print(f"No hay lugar para colocar una reina en columna {k}. Retrocediendo a la columna anterior...")
            k -= 1  

    print("No se encontró ninguna solución.")
    return False  
resultado = cuatro_reinas()
print("Hay solución" if resultado else "No hay solución")
