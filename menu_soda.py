import os # sistema operatio
class menu_soda:

    # Se inicializa los atributos o estado de objetos.
    def __init__(self):
        # constantes de dato entero como atributos.
        self.HAMBURGUESA = 1500
        self.EMPANADA = 1300
        self.TACOS = 1000
        self.FRESCO = 800
        self.GASEOSA = 1200

    def mostrar_matriz(self, tamannio):

        while True:
            os.system("cls")

            # Llenado previo de la matriz  de dato cadena de 5 filas por 3 columnas
            matriz = [["01", "Hamburguesa", "1500"],
                      ["02", "Empanada", "1300"],
                      ["03", "Tacos", "1000"],
                      ["04", "Fresco natural", "800"],
                      ["05", "Gaseosas", "1200"]]
            print("*****************************")
            print("  MENU DE LA SODA EL COLE   *")
            print("*****************************\n")

            # Impresión de matriz  con valores
            for i in matriz: # i es igual a fila
                print(i)
            print("\n---> Presione 6 para salir")
            compra = input("Digite la opción para comprar: ")

            if compra == '1': # observar la opción hamburguesa
                os.system("cls")
                print("*************************")
                print("*     HAMBURGUESAS      *")
                print("*************************\n")
                cantidad = int(input("Digite la cantidad de hamburguesas que desea comprar: "))
                precio = cantidad * self.HAMBURGUESA
                print(f"La cantidad que desea comprar es: {cantidad}")
                print(f"El precio de las hamburguesas es: {precio}")
                print("")
                input("Digite enter para volver...")


            elif compra == '2': # observar la opción empanada
                os.system("cls")
                print("*************************")
                print("*       EMPANADAS       *")
                print("*************************\n")
                cantidad = int(input("Digite la cantidad de empanadas: "))
                precio = cantidad * self.EMPANADA
                print(f"La cantidad que desea comprar es: {cantidad}")
                print(f"El precio de las empanadas es: {precio}")
                print("")
                input("Digite enter para volver...")

            elif compra == '3': # observar la opción tacos
                os.system("cls")
                print("*************************")
                print("*        TACOS          *")
                print("*************************\n")
                cantidad = int(input("Digite la cantidad de tacos: "))
                precio = cantidad * self.TACOS
                print(f"La cantidad que desea comprar es: {cantidad}")
                print(f"El precio de las tacos es: {precio}")
                print("")
                input("Digite enter para volver...")

            elif compra == '4': # observar la opción de los frescoa naturales
                os.system("cls")
                print("*************************")
                print("*    FRESCO NATURAL     *")
                print("*************************\n")
                cantidad = int(input("Digite la cantidad de frescos: "))
                precio = cantidad * self.FRESCO
                print(f"La cantidad que desea comprar es: {cantidad}")
                print(f"El precio de los frescos es: {precio}")
                print("")
                input("Digite enter para volver...")

            elif compra == '5': # observar la opción de gaseosas
                os.system("cls")
                print("*************************")
                print("*      GASEOSAS         *")
                print("*************************\n")
                cantidad = int(input("Digite la cantidad de gaseosas: "))
                precio = cantidad * self.GASEOSA
                print("")
                print(f"La cantidad que desea comprar es: {cantidad}")
                print(f"El precio de las gaseosas es: {precio}")
                input("Digite enter para volver...")

            elif compra == '6': #salir
                break

            else:
                print("Error...")
                input("Presione enter para volver")