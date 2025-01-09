
### LOOPS ###

# while

my_condition = 0

# while True:
#     print(my_condition)
#     my_condition += 12
# # else:  # es opcional
# #     print("Mi condicion es mayor o igual a 10")

# my_condition = 0
# while my_condition < 20:
#     my_condition += 1
#     if my_condition == 15:
#         print(my_condition)
#         print("Se detiene la ejecucion")
#         break
#     print(my_condition)

# print("Fin de Programa")

# Tabla del 8
# print("--------------------------")
# numero = int(
#     input("Dame un numero, no letras para la crear la tabla de multiplicar: "))
# print("------------------------------")
# print("------------------------------")
# print(f"           TABLA DEL {numero}        ")
# print("------------------------------")
# print("------------------------------")
# contador = 0
# while contador < 10:
#     contador += 1
#     resultado = contador*numero
#     print(f"{contador} x {numero} = {resultado}")
# print("Fin de Programa")

# For

# my_tupla = ("8x1=8", 34, 45, 67, 80, 23, 6)

# for item in my_tupla:
#     item = item * 8
#     print(item)

# my_set = {"8x1=8", 34, 45, 67, 80, 23, 6}

# for item in my_set:
#     item = item * 8
#     print(item)

my_dict = {"Nombre": "Pepe", 34: "Hola"}


# for item in my_dict:
#     print(f"Dentro de item hay: {item}")
#     print(f" El valor para la calve {item} es {my_dict[item]}")


for item in my_dict:
    if item == "Nombre":
        print("Econtrado la clave nombre en dicionario")

