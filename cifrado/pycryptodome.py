from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generar clave y vector de inicialización (IV)
clave = get_random_bytes(16)
cipher = AES.new(clave, AES.MODE_EAX)

texto = "Hola, esto es un mensaje secreto"


# Cifrar mensaje
caja = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")
cifrado, tag = cipher.encrypt_and_digest(caja)

print("Texto Cifrado:", cifrado)

# Descifrar mensaje
cipher_dec = AES.new(clave, AES.MODE_EAX, cipher.nonce)
mensaje_descifrado = cipher_dec.decrypt(cifrado).decode()
print("Texto Descifrado:", mensaje_descifrado)
