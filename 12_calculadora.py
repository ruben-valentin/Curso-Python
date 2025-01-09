# Imprimir por pantalla un menu para poder
# Seleccionar una de las siguientes operaciones:
# suma, resta, multiplicacion y division
# El programa pedira dos numeros por pantalla
# y mostrara el resultado final de la operacion

def suma(numero1, numero2):
    return numero1 + numero2


def resta(numero1, numero2):
    return numero1 - numero2


def division(numero1, numero2):
    return numero1 / numero2


def multiplicacion(numero1, numero2):
    return numero1 * numero2


def mostrar_menu():
    print("--------------------------")
    print("=== CALCULADORA BASICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


def seleccionar_opcion():
    opcion = input("\nElige una opción (1-5):")
    return opcion

# Función para pedir números


def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    return num1, num2


def calculadora():
    while True:
        mostrar_menu()
        opcion = seleccionar_opcion()

        if opcion == "5":
            print("\n Bye Bye")
            break
        # Para cualquier operación, necesitamos dos números
        if opcion in ["1", "2", "3", "4"]:
            num1, num2 = pedir_numeros()

            # Realizamos la operación según la opción elegida
            if opcion == "1":
                resultado = suma(num1, num2)
                print(f"\nLa suma es: {resultado}")

            elif opcion == "2":
                resultado = resta(num1, num2)
                print(f"\nLa resta es: {resultado}")

            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
                print(f"\nLa multiplicación es: {resultado}")

            elif opcion == "4":
                # Comprobamos que no se divida por cero
                if num2 == 0:
                    print("\nError: No se puede dividir por cero")
                else:
                    resultado = division(num1, num2)
                    print(f"\nLa división es: {resultado}")
        else:
            print("\nError: Opción no válida")
        input("Presiona Enter para continuar...")


#  CALULADORA

calculadora()
