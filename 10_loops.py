
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
print("--------------------------")
numero = int(
    input("Dame un numero, no letras para la crear la tabla de multiplicar: "))
print("------------------------------")
print("------------------------------")
print(f"           TABLA DEL {numero}        ")
print("------------------------------")
print("------------------------------")
contador = 0
while contador < 10:
    contador += 1
    resultado = contador*numero
    print(f"{contador} x {numero} = {resultado}")
print("Fin de Programa")
