# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema

# Importamos las funciones de cifrado y descifrado
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Título de la aplicación en la interfaz de Streamlit
st.title("Cifrado Pycryptodome - Codificación y Decodificación")

# Inicializar variables de sesión en Streamlit para mantener el estado entre interacciones
if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

# Generar clave y vector de inicialización (IV)
if "clave" not in st.session_state:
    st.session_state.clave = get_random_bytes(16)  # Inicializamos una variable para guardar la clave

if "cipher" not in st.session_state:
    st.session_state.cipher = AES.new(st.session_state.clave, AES.MODE_EAX)  # Inicializamos una variable para guardar cipher

# Sección para subir un archivo de texto
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_1")


# Verificamos si el usuario ha subido un archivo
if archivo:
    texto = archivo.read().decode("utf-8")  # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    st.text_area("Contenido del archivo:", texto, height=200)  # Mostramos el contenido en un área de texto
    st.session_state.texto_cifrado = texto
    st.markdown(f"**Texto a cifrar:** `{st.session_state.texto_cifrado}`")


    # Botón para cifrar el texto
    if st.button("Cifrar"):
      # CIFRAR
        caja = st.session_state.texto_cifrado.encode()
        cifrado, tag = st.session_state.cipher.encrypt_and_digest(caja)
        st.markdown(f" ------------")
        st.markdown(f"**Texto cifrado:** `{cifrado}`")
      # Guardamos el texto descifrado en un archivo dentro de la carpeta "archivos"
        with open("archivos/cifrado.txt", "wb") as f:
            f.write(cifrado)

    #  st.markdown(f"**Texto a descifrar:** `{st.session_state.texto_cifrado}`")

    # Botón para descifrar el texto
    if st.button("Descifrar"):
       # Descifrar
        st.markdown(f"Aqui texto decifrado")
        # Descifrar
        cipher_dec = AES.new(st.session_state.clave, AES.MODE_EAX, st.session_state.cipher.nonce)
        mensaje_descifrado = cipher_dec.decrypt(st.session_state.texto_cifrado ).decode()

        st.markdown(f"**Texto cifrado:** `{st.session_state.texto_cifrado}`")
        # cipher_dec = AES.new(st.session_state.clave, AES.MODE_EAX, st.session_state.cipher.nonce)
        # mensaje_descifrado = cipher_dec.decrypt(st.session_state.texto_cifrado).decode()
