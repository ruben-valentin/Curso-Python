# cesar.py

# Definir el alfabeto español con la ñ incluida
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
ALFABETO_MAYUS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter in ALFABETO:  # Si es una letra minúscula
            indice = (ALFABETO.index(caracter) + desplazamiento) % 27
            resultado += ALFABETO[indice]
        elif caracter in ALFABETO_MAYUS:  # Si es una letra mayúscula
            indice = (ALFABETO_MAYUS.index(caracter) + desplazamiento) % 27
            resultado += ALFABETO_MAYUS[indice]
        else:
            resultado += caracter  # Mantener espacios y signos sin cambios
    return resultado

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter in ALFABETO:  # Si es una letra minúscula
            indice = (ALFABETO.index(caracter) - desplazamiento) % 27
            resultado += ALFABETO[indice]
        elif caracter in ALFABETO_MAYUS:  # Si es una letra mayúscula
            indice = (ALFABETO_MAYUS.index(caracter) - desplazamiento) % 27
            resultado += ALFABETO_MAYUS[indice]
        else:
            resultado += caracter  # Mantener espacios y signos sin cambios
    return resultado
