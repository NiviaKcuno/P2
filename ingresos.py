import os #llamado al sistema operativo
class ingresos: #clases

    def __init__(self): # atributo
        self.vectorIngresos = [0] * 7 #dimensión del vector

    def llenar_vector(self): #función o método para el llenado del vector
        for i in range(7): #i es la fila
            monto = int(input(f"Digite el monto diario de ingresos {i}: "))
            self.vectorIngresos[i] = monto

    def imprimir_vector(self):
        print("Vector de ingreso semanal actual:", self.vectorIngresos)
        input("Presione enter para continuar...")

    def modificar_vector(self):
        os.system("cls")
        print("Ingrese la cantidad ingreso de dinero de lunes a sábado")

        indiceNuevo = int(input("Digite el índice que desea cambiar (0-6): "))
        if 0 <= indiceNuevo < 7:
            montoDiario = int(input(f"Digite el monto para el indice {indiceNuevo}: "))
            self.vectorIngresos[indiceNuevo] = montoDiario
            print(f"Valor en el indice {indiceNuevo} actualizado.")
        else:
            print("Indice no existe")

        print("Lista actualizada:", self.vectorIngresos)
        input("Presione enter para continuar...")

    # función que asigna valores de cero al indice que el usuario desea borrar.
    def borrar_vector(self):
        os.system("cls")

        # variable que almacena el indice del vector para aplicar el borrado.
        indiceBorrado = int(input("Digite el indice que desea borrar (0-6): "))

        if 0 <= indiceBorrado < 7: #  el vector cuenta con un rango de indices (0-7).
            self.vectorIngresos[indiceBorrado] = 0
            print(f"El monto de {indiceBorrado} ha sido borrado.")
        else:
            print("Indice no existe")      # Instrucción para indices que se digitan y no existen.
        print("Indice borrado:", self.vectorIngresos)   # Impresion de vector con el borrado aplicado.
        input("Presione enter para continuar...") # Esperar tecla por medio de entrada de datos.

    # Función que suma y que almacena el vector.
    def sumar_vector(self):
        total = sum(self.vectorIngresos) # almacena el resultado de la suma .

        # Impresion del resultado de la suma.
        print(f"La suma total de los valores en el vector es: {total}")
        input("Presione enter para continuar...")  # Esperar tecla por medio de entrada de datos.


    def menuRegistroIngresos(self): # menu de los ingresos semanales
        while True:
            os.system('cls')    # Limpiar pantalla de consola.
            print("1. Llenar lista de ingresos semanales")
            print("2. Imprimir ingresos")
            print("3. Actualizar monto")
            print("4. Borrar monto")
            print("5. Suma total de ingresos")
            print("6. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == '1':
                self.llenar_vector()  #llenar el vector con el uso de ciclo for.

            elif opcion == '2':
                self.imprimir_vector() #la función de impresión de vector.

            elif opcion == '3':
                self.modificar_vector()   #Llamada a función de modificar el vector

            elif opcion == '4':
                self.borrar_vector() #Llamada a función de borrar

            elif opcion == '5':
                self.sumar_vector()   #función de cálculo de suma

            elif opcion == '6':
                break  # Salir del bucle

            else: #Opción para errores en la selección de opcion del submenu.
                os.system("cls")
                print("Error al ingresar opcion")
                input("Presione enter para continuar...")
                pass

class vectorHerencia(ingresos):
    pass