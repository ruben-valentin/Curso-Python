# cesar.py

# Definir el alfabeto español con la letra 'ñ' incluida
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
ALFABETO_MAYUS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar_cesar(texto, desplazamiento):
    """
    Cifra un texto utilizando el Cifrado César.

    Parámetros:
    texto (str): El texto a cifrar.
    desplazamiento (int): El número de posiciones a desplazar en el alfabeto.

    Retorna:
    str: El texto cifrado.
    """
    resultado = ""  # Variable donde se almacenará el texto cifrado

    for caracter in texto:  # Recorre cada caracter del texto de entrada
        if caracter in ALFABETO:  # Si el caracter es una letra minúscula
            # Obtiene el nuevo índice después del desplazamiento, asegurando que se mantenga en el rango del alfabeto (mod 27)
            indice = (ALFABETO.index(caracter) + desplazamiento) % 27
            resultado += ALFABETO[indice]  # Agrega la letra cifrada al resultado

        elif caracter in ALFABETO_MAYUS:  # Si el caracter es una letra mayúscula
            # Obtiene el nuevo índice después del desplazamiento para mayúsculas
            indice = (ALFABETO_MAYUS.index(caracter) + desplazamiento) % 27
            resultado += ALFABETO_MAYUS[indice]  # Agrega la letra cifrada al resultado

        else:
            # Si el caracter no es una letra (espacios, signos de puntuación, números, etc.), se deja igual
            resultado += caracter

    return resultado  # Retorna el texto ya cifrado


def descifrar_cesar(texto, desplazamiento):
    """
    Descifra un texto previamente cifrado con el Cifrado César.

    Parámetros:
    texto (str): El texto cifrado a descifrar.
    desplazamiento (int): El número de posiciones a retroceder en el alfabeto.

    Retorna:
    str: El texto descifrado.
    """
    resultado = ""  # Variable donde se almacenará el texto descifrado

    for caracter in texto:  # Recorre cada caracter del texto cifrado
        if caracter in ALFABETO:  # Si el caracter es una letra minúscula
            # Obtiene el índice original restando el desplazamiento, asegurando que se mantenga en el rango del alfabeto (mod 27)
            indice = (ALFABETO.index(caracter) - desplazamiento) % 27
            resultado += ALFABETO[indice]  # Agrega la letra descifrada al resultado

        elif caracter in ALFABETO_MAYUS:  # Si el caracter es una letra mayúscula
            # Obtiene el índice original restando el desplazamiento para mayúsculas
            indice = (ALFABETO_MAYUS.index(caracter) - desplazamiento) % 27
            resultado += ALFABETO_MAYUS[indice]  # Agrega la letra descifrada al resultado

        else:
            # Si el caracter no es una letra (espacios, signos de puntuación, números, etc.), se deja igual
            resultado += caracter

    return resultado  # Retorna el texto ya descifrado
