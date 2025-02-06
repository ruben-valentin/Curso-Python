# ⚡ Cifrado y Descifrado en Python con `pycryptodome`

La librería **`pycryptodome`** proporciona algoritmos criptográficos modernos para cifrado y descifrado en Python. Soporta **AES, RSA, SHA, HMAC**, entre otros.

---

## **🔒 Tipos de Cifrado en `pycryptodome`**

### **1. Cifrado Simétrico** (Usa la misma clave para cifrar y descifrar)
- **AES (Advanced Encryption Standard)** 🛡️ *(recomendado)*
- **DES y Triple DES (3DES)** *(obsoleto, no recomendado)*
- **ChaCha20** *(rápido y seguro)*

### **2. Cifrado Asimétrico** (Usa una clave pública y una privada)
- **RSA** *(muy usado en HTTPS, SSH, PGP)*
- **ECC (Elliptic Curve Cryptography)** *(más eficiente que RSA)*

### **3. Funciones Hash** (Para verificar integridad de datos)
- **SHA-256, SHA-512** *(seguros, ampliamente usados)*
- **HMAC (Hash-based Message Authentication Code)** *(autenticación de datos)*

### **4. Firmas Digitales** (Verificación de autenticidad)
- **RSA, DSA, ECDSA** *(para firmar y verificar datos)*

---

## **1️⃣ Cifrado Simétrico (AES, DES, ChaCha20)**

### **🔹 AES (Advanced Encryption Standard)**

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generar clave y vector de inicialización (IV)
clave = get_random_bytes(16)  # AES-128 usa 16 bytes
iv = get_random_bytes(16)

# Crear cifrador
cipher = AES.new(clave, AES.MODE_CBC, iv)

# Cifrar
mensaje = "Mensaje secreto".encode().ljust(16)  # Asegurar que sea múltiplo de 16
texto_cifrado = cipher.encrypt(mensaje)
print("AES Cifrado:", texto_cifrado)

# Descifrar
decipher = AES.new(clave, AES.MODE_CBC, iv)
mensaje_descifrado = decipher.decrypt(texto_cifrado).strip()
print("AES Descifrado:", mensaje_descifrado.decode())
```

---

### **🔹 Cifrado RSA (Clave Pública y Privada)**

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generar claves
clave = RSA.generate(2048)
clave_privada = clave.export_key()
clave_publica = clave.publickey().export_key()

# Cifrar
mensaje = "Mensaje seguro con RSA".encode()
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(clave_publica))
cifrado = cipher_rsa.encrypt(mensaje)
print("RSA Cifrado:", cifrado)

# Descifrar
decipher_rsa = PKCS1_OAEP.new(RSA.import_key(clave_privada))
descifrado = decipher_rsa.decrypt(cifrado)
print("RSA Descifrado:", descifrado.decode())
```

---

## **2️⃣ Funciones Hash (SHA-256, SHA-512, HMAC)**

```python
from Crypto.Hash import SHA256, HMAC

# SHA-256
mensaje = b"Mensaje para hash"
digest = SHA256.new(mensaje)
print("SHA-256 Hash:", digest.hexdigest())

# HMAC (Hash con Clave)
clave = b"clave_secreta"
hmac = HMAC.new(clave, mensaje, SHA256)
print("HMAC SHA-256:", hmac.hexdigest())
```

---

## **🔍 Comparación de Algoritmos**

| Algoritmo  | Tipo | Seguridad | Velocidad |
|------------|------|-----------|-----------|
| **AES** | Simétrico | 🛡️🛡️🛡️🛡️🛡️ | 🚀🚀🚀 |
| **ChaCha20** | Simétrico | 🛡️🛡️🛡️🛡️ | 🚀🚀🚀🚀 |
| **RSA** | Asimétrico | 🛡️🛡️🛡️🛡️ | 🐢🐢 |
| **SHA-256** | Hash | 🛡️🛡️🛡️🛡️🛡️ | 🚀🚀🚀🚀🚀 |

---

## **🚀 Conclusión**
- **AES-256 + CBC** o **ChaCha20** → Para almacenar datos cifrados de forma segura.
- **RSA** → Para cifrado de claves en comunicación (HTTPS, SSH).
- **SHA-256** → Para proteger contraseñas y verificar integridad de datos.

