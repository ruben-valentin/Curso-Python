from cryptography.fernet import Fernet

# 1. Generar una clave secreta
clave = Fernet.generate_key()
cipher = Fernet(clave)

texto = "Hola, esto es un mensaje secreto"

# 2. Cifrar un mensaje
mensaje = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")

mensaje_cifrado = cipher.encrypt(mensaje)
print("Mensaje Cifrado:", mensaje_cifrado)

# 3. Descifrar el mensaje
mensaje_descifrado = cipher.decrypt(mensaje_cifrado).decode()
print("Mensaje Descifrado:", mensaje_descifrado)
