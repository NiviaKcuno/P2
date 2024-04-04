import os

class inventario_soda:
    # Patrón singleton para la matriz de inventario
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.matriz = []

    def dimensionar_matriz(self): #el usuario indica la dimensión de la matriz
        os.system("cls")
        print("Ingrese las dimensiones de la matriz:")
        fila = int(input("Número de filas: "))
        columna = int(input("Número de columnas: "))
        self.matriz = [['' for _ in range(columna)] for _ in range(fila)]
        print("Llene el registro con su informacion (ingrese cada elemento por fila)")
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                valor = input(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): ")
                self.matriz[i][j] = valor

    def imprimir_matriz(self): # ver el llenado de la matriz
        os.system("cls")
        print("Matriz actual:")
        for fila in self.matriz:
            print(fila)
        input("Presione enter para continuar...")

    def actualizar_matriz(self): #actualizar una posición de l matriz
        os.system("cls")
        print("Ingrese la fila y columna que desea actualizar")

        actualizar_fila = int(input("Ingrese la fila que desea actualizar (0-%d): " % (len(self.matriz)-1)))
        actualizar_columna = int(input("Ingrese la columna que desea actualizar (0-%d): " % (len(self.matriz[0])-1)))

        if 0 <= actualizar_fila < len(self.matriz) and 0 <= actualizar_columna < len(self.matriz[0]):
            valor_actualizar = input(f"Ingrese el valor para la posición ({actualizar_fila}, {actualizar_columna}): ")
            self.matriz[actualizar_fila][actualizar_columna] = valor_actualizar
            print("Valor actualizado.")
        else:
            print("Error, no exite la posición")

        self.imprimir_matriz()

    def borrar_matriz(self): # borrar una sección de la matriz
        os.system("cls")
        fila_borrar = int(input("Ingrese la fila que desea borrar (0-%d): " % (len(self.matriz)-1)))
        columna_borrar = int(input("Ingrese la columna que desea borrar (0-%d): " % (len(self.matriz[0])-1)))

        if 0 <= fila_borrar < len(self.matriz) and 0 <= columna_borrar < len(self.matriz[0]):
            self.matriz[fila_borrar][columna_borrar] = ""
        else:
            print("Posición no existe")

        self.imprimir_matriz()

    def menu_inventario(self): #menú del inventario
        while True:
            os.system('cls')
            print("1. Dimension y llenado de inventario")
            print("2. Imprimir matriz")
            print("3. Actualizar valor en posición")
            print("4. Borrar valor en posición")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            # llamado de las funciones o métodos
            if opcion == '1':
                self.dimensionar_matriz()

            elif opcion == '2':
                self.imprimir_matriz()

            elif opcion == '3':
                self.actualizar_matriz()

            elif opcion == '4':
                self.borrar_matriz()

            elif opcion == '5':
                break  # Salir del ciclo

            else:
                os.system("cls")
                print("Error al ingresar opción")
                input("Presione enter para continuar...")
                pass

