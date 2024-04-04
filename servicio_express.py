import os
class servicio_express:
    # constantes
    def __init__(self):
        self.ARROZCANT = 4000 # precio del arroz cantones
        self.RB = 3500 # precio del rice and beans
        self.ARROZCAM = 6000 # precio del arroz con camarones
        self.DESCUENTO1 = 0.15
        self.DESCUENTO2 = 0.10
        self.DESCUENTO3 = 0.05

    def express(self): # submenu de la opción 3
        while True:
            os.system('cls') # limpiar consola
            print("Seleccione la compra")
            print("1. Arroz cantones 4000")
            print("2. Rice beans 3500")
            print("3. Arroz con camarones 6000")
            print("4. Salir")

            opc = input("Digite el servicio a comprar: ")

            if opc == '1': #opción 1

                os.system('cls')
                print("El precio del arroz cantones es 4000 colones")
                cant1 = int(input("Digite la cantidad a comprar: "))

                # Estructura anidada con tres condiciones compuestas
                if 11 >= cant1 >= 8: #  calcula la cantidad del pedido del servicio express y aplicar un descuento
                    prec1 = cant1 * self.ARROZCANT
                    valordescontado = prec1 * self.DESCUENTO1
                    Total = prec1 - valordescontado
                    print(f"El precio unitario de su compra es de {self.ARROZCANT}")
                    print(f"El precio de su compra total sin descuento: {prec1}")
                    print(f"El valor del descuento es: {self.DESCUENTO1}")
                    print(f"El monto del descuento: {valordescontado}")
                    print(f"El total a pagar es: {Total}")

                elif 8 > cant1 >= 5:
                    prec1 = cant1 * self.ARROZCANT
                    valordescontado = prec1 * self.DESCUENTO2
                    Total = prec1 - valordescontado
                    print(f"El precio unitario de su compra es de {self.ARROZCANT}")
                    print(f"El precio de su compra total sin descuento: {prec1}")
                    print(f"El valor del descuento es: {self.DESCUENTO2}")
                    print(f"El monto del descuento: {valordescontado}")
                    print(f"El total a pagar es: {Total}")

                elif 5 > cant1 >= 2:
                    prec1 = cant1 * self.ARROZCANT
                    valordescontado = prec1 * self.DESCUENTO3
                    Total = prec1 - valordescontado
                    print(f"El precio unitario de su compra es de {self.ARROZCANT}")
                    print(f"El precio de su compra total sin descuento: {prec1}")
                    print(f"El valor del descuento es: {self.DESCUENTO3}")
                    print(f"El monto del descuento: {valordescontado}")
                    print(f"El total a pagar es: {Total}")

                else:
                    print("La compra no cumple con el descuento")

                input("Presione enter para continuar...")

            elif opc == '2':

                os.system('cls')
                print("El precio del rice and  beans es 3500 colones")
                cant2 = int(input("Digite la cantidad a comprar: "))

                # Estructura anidada con tres condiciones compuestas
                if 11 >= cant2 >= 8:
                    prec2 = cant2 * self.RB
                    valordescontado2 = prec2 * self.DESCUENTO1
                    Total2 = prec2 - valordescontado2
                    print(f"El precio unitario de su compra es de {self.RB}")
                    print(f"El precio de su compra total sin descuento: {prec2}")
                    print(f"El valor del descuento es: {self.DESCUENTO1}")
                    print(f"El monto del descuento: {valordescontado2}")
                    print(f"El total a pagar es: {Total2}")

                elif 8 > cant2 >= 5:
                    prec2 = cant2 * self.RB
                    valordescontado2 = prec2 * self.DESCUENTO2
                    Total2 = prec2 - valordescontado2
                    print(f"El precio unitario de su compra es de {self.RB}")
                    print(f"El precio de su compra total sin descuento: {prec2}")
                    print(f"El valor del descuento es: {self.DESCUENTO2}")
                    print(f"El monto del descuento: {valordescontado2}")
                    print(f"El total a pagar es: {Total2}")

                elif 5 > cant2 >= 2:
                    prec2 = cant2 * self.RB
                    valordescontado2 = prec2 * self.DESCUENTO3
                    Total2 = prec2 - valordescontado2
                    print(f"El precio unitario de su compra es de {self.RB}")
                    print(f"El precio de su compra total sin descuento: {prec2}")
                    print(f"El valor del descuento es: {self.DESCUENTO3}")
                    print(f"El monto del descuento: {valordescontado2}")
                    print(f"El total a pagar es: {Total2}")

                else:
                    print("La compra no cumple con el descuento")

                input("Presione enter para continuar...")

            elif opc == '3':

                os.system('cls')
                print("El precio del arroz con  camarones es 6000 colones")
                cant3 = int(input("Digite la cantidad a comprar: "))

                # Estructura anidada con tres condiciones compuestas
                if 11 >= cant3 >= 8:
                    prec3 = cant3 * self.ARROZCAM
                    valordescontado3 = prec3 * self.DESCUENTO1
                    Total3 = prec3 - valordescontado3
                    print(f"El precio de su compra es de {self.ARROZCAM}")
                    print(f"El precio de su compra total sin descuento: {prec3}")
                    print(f"El valor del descuento es: {self.DESCUENTO1}")
                    print(f"El monto del descuento: {valordescontado3}")
                    print(f"El total a pagar es: {Total3}")

                elif 8 > cant3 >= 5:
                    prec3 = cant3 * self.ARROZCAM
                    valordescontado3 = prec3 * self.DESCUENTO2
                    Total3 = prec3 - valordescontado3
                    print(f"El precio de su compra es de {self.ARROZCAM}")
                    print(f"El precio de su compra total sin descuento: {prec3}")
                    print(f"El valor del descuento es: {self.DESCUENTO2}")
                    print(f"El monto del descuento es: {valordescontado3}")
                    print(f"El total a pagar es: {Total3}")

                elif 5 > cant3 >= 2:
                    prec3 = cant3 * self.ARROZCAM
                    valordescontado3 = prec3 * self.DESCUENTO3
                    Total3 = prec3 - valordescontado3
                    print(f"El precio unitario de su compra es de {self.ARROZCAM}")
                    print(f"El precio de su compra total sin descuento: {prec3}")
                    print(f"El valor del descuento es: {self.DESCUENTO3}")
                    print(f"El monto del descuento: {valordescontado3}")
                    print(f"El total a pagar es: {Total3}")

                else:
                    print("La compra no cumple con el descuento")

                input("Presione enter para continuar...")

            elif opc == '4': # salir
                break

            else:
                os.system("cls")
                print("Error al ingresar opción")
                input("Presione enter para continuar...")
