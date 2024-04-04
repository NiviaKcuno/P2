#Proyecto 1 Nivia Kcuno
#llamano de las clases
from menu_soda import menu_soda
from servicio_express import *
from inventario_soda import inventario_soda
from ingresos import vectorHerencia
import os

if __name__ == '__main__': # para iniciar el menú

    while True:

        os.system('cls') #limpiar consola

        # Impresión del menú inicial
        print('Hola Bienvenidos a la Soda EL Cole:')
        print('Seleccione una opción:')
        print('1. Ver el menú de la soda')
        print('2. Inventario de soda')
        print('3. Servicio express')
        print('4. Ver ingresos semanales')
        print('5. Salir')

        opcion = input('Ingrese la opción a realizar -> ')

        # Mostrar la matriz del menú
        if opcion == '1':
            menu_soda1 = menu_soda()
            menu_soda1.mostrar_matriz(4)

            input("Digite enter para volver...")

        # Indiar la dimesión necesaria para luego crear el inventario de los productos
        elif opcion == '2':
            os.system('cls')
            inventario_soda1 = inventario_soda()
            inventario_soda1.menu_inventario()
            input("Digite enter para volver...")

        # Realizar descuentos con las compras de servicio express
        elif opcion == '3':
            os.system('cls')
            servicio_express1 = servicio_express()
            servicio_express1.express()

            input("Digite enter para volver...")

        # Realizar los ingresos de las ventas diarios, a través de una herencia.
        elif opcion == '4':

            # ingresos1 = ingresos()
            # ingresos1.menuRegistroIngresos()

            # Creación de tres objetos de la clase vectorHerencia
            Juan = vectorHerencia()
            Maria = vectorHerencia()
            Diana = vectorHerencia()

            # Llamar al menú de registro de ingresos para cada objeto
            Juan.menuRegistroIngresos()
            Maria.menuRegistroIngresos()
            Diana.menuRegistroIngresos()

            input("Digite enter para volver...")

        elif opcion == '5': # salir de las opciones
            os.system('cls')
            break

        else:
            print("Error al digitar la opción")
            input("Presione enter para volver")
