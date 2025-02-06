# 🔐 Cifrado y Descifrado con Cryptography (Fernet)

Este documento explica cómo cifrar y descifrar un mensaje en Python usando **Fernet**, un sistema de cifrado simétrico basado en **AES-128**.

---

## 📌 Código Explicado Línea por Línea

### **1️⃣ Importar la Librería**
```python
from cryptography.fernet import Fernet
```
📌 **Importamos la clase `Fernet`** desde la librería `cryptography`.  
👉 `Fernet` usa **AES en modo CBC** con autenticación para garantizar la seguridad de los datos.

---

### **2️⃣ Generar una Clave Secreta**
```python
clave = Fernet.generate_key()
```
📌 **Generamos una clave secreta aleatoria** para cifrar y descifrar el mensaje.  
🔑 La clave es un string en formato `bytes` que debe **guardarse** para poder descifrar más tarde.

```python
cipher = Fernet(clave)
```
📌 **Creamos un objeto `Fernet`** con la clave generada.  
🔐 Este objeto (`cipher`) se usará para **cifrar y descifrar datos**.

---

### **3️⃣ Definir el Mensaje Original**
```python
texto = "Hola, esto es un mensaje secreto"
```
📌 **Definimos el mensaje que queremos cifrar** como una cadena de texto.

---

### **4️⃣ Cifrar un Mensaje**
```python
mensaje = texto.encode()
```
📌 **Convertimos el texto a `bytes`** porque `Fernet` solo trabaja con datos binarios.  
👉 `.encode()` transforma el string en **UTF-8 bytes**.

```python
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")
```
📌 **Mostramos el mensaje original** antes de cifrarlo.

```python
mensaje_cifrado = cipher.encrypt(mensaje)
```
📌 **Ciframos el mensaje con `cipher.encrypt()`**.  
🔒 `encrypt()` toma los datos en **bytes** y devuelve **un texto cifrado** en **base64**.

```python
print("Mensaje Cifrado:", mensaje_cifrado)
```
📌 **Mostramos el mensaje cifrado** en la consola.  
🚫 **Este mensaje es ilegible hasta que se descifre con la misma clave**.

---

### **5️⃣ Descifrar el Mensaje**
```python
mensaje_descifrado = cipher.decrypt(mensaje_cifrado).decode()
```
📌 **Desciframos el mensaje con `cipher.decrypt()`**.  
🔓 `decrypt()` **toma el mensaje cifrado y lo devuelve en `bytes`**.  
👉 `.decode()` lo convierte de **bytes a string** para que podamos leerlo.

```python
print("Mensaje Descifrado:", mensaje_descifrado)
```
📌 **Mostramos el mensaje descifrado** en la consola.  
🎯 **Debe coincidir con el mensaje original**:
```
"Hola, esto es un mensaje secreto"
```

---

## ✅ **Resumen del Funcionamiento**
1. **Se genera una clave secreta** (`Fernet.generate_key()`).
2. **Se crea un objeto `Fernet`** con la clave.
3. **Se convierte el mensaje a `bytes`** antes de cifrarlo.
4. **Se cifra el mensaje con `cipher.encrypt()`**.
5. **Se descifra con `cipher.decrypt()`** y se convierte de nuevo en texto legible.

---

## 🔥 **Ejemplo de Salida en la Consola**
```
-----------------------------------
Mensaje a Cifrar: Hola, esto es un mensaje secreto
-----------------------------------
Mensaje Cifrado: b'gAAAAABl... (texto en base64)'
Mensaje Descifrado: Hola, esto es un mensaje secreto
```
📌 El **mensaje cifrado** es ilegible porque está encriptado.  
📌 El **mensaje descifrado** coincide con el original.

🚀 **¡Listo! Ahora entiendes cómo funciona el cifrado y descifrado con `Fernet`!** 🎯

# ⚡ Cifrado y Descifrado en Python con `cryptography`

La librería **`cryptography`** en Python proporciona varios tipos de cifrado, tanto **simétricos** como **asimétricos**, junto con herramientas para manejar **hashing, firmas digitales y certificados**.

---

## 🔒 Tipos de Cifrado en `cryptography`

### **1. Cifrado Simétrico** (Usa la misma clave para cifrar y descifrar)
- **AES (Advanced Encryption Standard)** 🛡️ *(recomendado)*
- **ChaCha20** *(rápido y seguro)*
- **Fernet** *(fácil de usar, basado en AES)*
- **Triple DES (3DES)** *(obsoleto, no recomendado)*

### **2. Cifrado Asimétrico** (Usa una clave pública y una privada)
- **RSA** *(muy usado en comunicaciones seguras)*
- **Elliptic Curve Cryptography (ECC)** *(más eficiente que RSA)*
- **DSA (Digital Signature Algorithm)** *(firmas digitales, no cifrado)*

### **3. Funciones Hash** (Para verificar integridad de datos)
- **SHA-256, SHA-512** *(seguros, ampliamente usados)*
- **HMAC (Hash-based Message Authentication Code)** *(autenticación de datos)*

### **4. Firmas Digitales** (Verificación de autenticidad)
- **RSA, DSA, ECDSA** *(para firmar y verificar datos)*

---

## **1️⃣ Cifrado Simétrico (AES, ChaCha20, Fernet)**

### **🔹 AES (Advanced Encryption Standard)**

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from Crypto.Random import get_random_bytes

# Clave y vector de inicialización (IV)
clave = get_random_bytes(32)  # AES-256 usa 32 bytes
iv = get_random_bytes(16)  # Bloques de 16 bytes

# Crear el cifrador
cipher = Cipher(algorithms.AES(clave), modes.CBC(iv))

# Cifrar
encryptor = cipher.encryptor()
texto = "Mensaje secreto".encode()

# Rellenar el mensaje para que sea múltiplo de 16 bytes
padder = padding.PKCS7(128).padder()
texto_padded = padder.update(texto) + padder.finalize()

texto_cifrado = encryptor.update(texto_padded) + encryptor.finalize()
print("AES Cifrado:", texto_cifrado)

# Descifrar
decryptor = cipher.decryptor()
texto_descifrado_padded = decryptor.update(texto_cifrado) + decryptor.finalize()

# Eliminar el padding
unpadder = padding.PKCS7(128).unpadder()
texto_descifrado = unpadder.update(texto_descifrado_padded) + unpadder.finalize()
print("AES Descifrado:", texto_descifrado.decode())
```

---

### **🔹 Fernet (AES + Autenticación, Fácil de Usar)**

```python
from cryptography.fernet import Fernet

# Generar una clave
clave = Fernet.generate_key()
cipher = Fernet(clave)

# Cifrar
mensaje = "Hola, este es un mensaje seguro".encode()
mensaje_cifrado = cipher.encrypt(mensaje)
print("Fernet Cifrado:", mensaje_cifrado)

# Descifrar
mensaje_descifrado = cipher.decrypt(mensaje_cifrado)
print("Fernet Descifrado:", mensaje_descifrado.decode())
```

---

## **2️⃣ Cifrado Asimétrico (RSA, ECC)**

### **🔹 RSA (Muy Usado en HTTPS, SSH, PGP)**

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generar claves
clave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
clave_publica = clave_privada.public_key()

# Cifrar con la clave pública
mensaje = b"Mensaje seguro con RSA"
texto_cifrado = clave_publica.encrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("RSA Cifrado:", texto_cifrado)

# Descifrar con la clave privada
texto_descifrado = clave_privada.decrypt(
    texto_cifrado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("RSA Descifrado:", texto_descifrado.decode())
```

---

## **3️⃣ Funciones Hash (SHA-256, SHA-512)**

```python
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"Mensaje para hash")
print("SHA-256 Hash:", digest.finalize().hex())
```

---

## **🔍 Comparación de Algoritmos**

| Algoritmo  | Tipo | Seguridad | Velocidad |
|------------|------|-----------|-----------|
| **AES** | Simétrico | 🛡️🛡️🛡️🛡️🛡️ | 🚀🚀🚀 |
| **ChaCha20** | Simétrico | 🛡️🛡️🛡️🛡️ | 🚀🚀🚀🚀 |
| **Fernet** | Simétrico | 🛡️🛡️🛡️ | 🚀🚀🚀 |
| **RSA** | Asimétrico | 🛡️🛡️🛡️🛡️ | 🐢🐢 |

---

## **🚀 Conclusión**
- **AES-256 + CBC** o **ChaCha20** → Para almacenar datos cifrados de forma segura.
- **Fernet** → Para cifrar datos fácilmente en una aplicación.
- **RSA** → Para cifrado de claves en comunicación (HTTPS, SSH).
- **SHA-256** → Para proteger contraseñas.

