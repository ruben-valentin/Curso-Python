# variables

pi = 3.14

# Funciones que no devuleven nada


def imprimir_hola_mundo():
    print("Hola Mundo")


# imprimir_hola_mundo()
# imprimir_hola_mundo()
# imprimir_hola_mundo()
# imprimir_hola_mundo()
# imprimir_hola_mundo()


def suma(var1: int, var2):
    print(var1+var2)


def sumar():
    var1 = int(input("Dame el primer numero: "))
    var2 = int(input("Dame el segundo numero: "))
    suma(var1, var2)


def multiplicar_por_pi_por_un_valor_dado(valor: int):
    print(valor*pi)


# suma(2, 5)
# suma(4, 3)
# suma(9, 20)
# suma(1, 3)
# sumar()
# multiplicar_por_pi_por_un_valor_dado(34)


def resta(var1, var2):
    resulado = var1-var2
    return resulado


# var3 = resta(4, 2)
# print(var3)

print(resta(4, 2))


def encriptar(texto):
    # hacer encriptacion
    return texto
