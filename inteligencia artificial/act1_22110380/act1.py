import array

class Articulo:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    def detalles(self):
        return f"'{self.titulo}' - Precio: ${self.precio:.2f}"

class Libro(Articulo):
    def __init__(self, titulo, precio, cantidad):
        super().__init__(titulo, precio)
        self.cantidad = cantidad
    
    def detalles(self):
        return f"'{self.titulo}' - Precio: ${self.precio:.2f} - Disponibles: {self.cantidad} ejemplar(es)"

class Libreria:
    def __init__(self):
        self.catalogo = [
            Libro("El amor en los tiempos del cólera - Gabriel García Márquez", 360, 4),
            Libro("1984 - George Orwell", 280, 7),
            Libro("Moby Dick - Herman Melville", 410, 2),
            Libro("Cumbres Borrascosas - Emily Brontë", 320, 5),
            Libro("El principito - Antoine de Saint-Exupéry", 200, 10),
            Libro("Homo Deus - Yuval Noah Harari", 480, 6),
        ]
        
        self.clasificacion = {
            "Novela": [self.catalogo[0], self.catalogo[2], self.catalogo[3]],
            "Ciencia Ficción": [self.catalogo[1]],
            "Filosofía y Historia": [self.catalogo[5]],
            "Literatura Infantil": [self.catalogo[4]]
        }

        self.array_stock = array.array('i', [libro.cantidad for libro in self.catalogo])

    generos = ("Novela", "Ciencia Ficción", "Filosofía y Historia", "Literatura Infantil")

    def mostrar_catalogo(self):
        print("\nCatálogo disponible:\n")
        for idx, libro in enumerate(self.catalogo):
            print(f"{idx + 1}. {libro.detalles()}")

    def procesar_compra(self, seleccion):
        articulo = self.catalogo[seleccion]
        if articulo.cantidad > 0:
            print(f"\nHa escogido: {articulo.titulo}.\n ¿Confirma la compra?")
            decision = input("Responda 'Sí' o 'No': ").lower()
            if decision in ['si', 'sí']:
                articulo.cantidad -= 1
                print(f"\n¡Compra exitosa! Ha adquirido: '{articulo.titulo}'. \nTotal: ${articulo.precio:.2f}.")
            else:
                print("\nCompra cancelada.")
        else:
            print("\nEste título está agotado.\n")

    def iniciar(self):
        while True:
            self.mostrar_catalogo()
            try:
                opcion = int(input("\nSeleccione el número del libro que desea adquirir o ingrese '0' para salir.\n"))
                if opcion == 0:
                    print("\n¡Gracias por su visita! Esperamos verle pronto...\n")
                    break
                elif 1 <= opcion <= len(self.catalogo):
                    self.procesar_compra(opcion - 1)
                else:
                    print("\nPor favor, seleccione una opción válida.\n")
            except ValueError:
                print("\nEntrada no válida. Ingrese un número por favor.\n")

# Ejecutar la librería
libreria = Libreria()
libreria.iniciar()
