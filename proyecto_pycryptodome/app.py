# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema
# Importamos las funciones de cifrado y descifrado
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generar clave y vector de inicialización (IV)
# clave = get_random_bytes(16)
# cipher = AES.new(clave, AES.MODE_EAX)

# Título de la aplicación en la interfaz de Streamlit
st.title("Cifrado Pycryptodome - Codificación y Decodificación")

# Inicializar variables de sesión en Streamlit para mantener el estado entre interacciones
if "clave" not in st.session_state:
    # Inicializamos una variable para guardar la clave
    st.session_state.clave = get_random_bytes(16)

if "cipher" not in st.session_state:
    # Inicializamos una variable para guardar el cipher
    st.session_state.cipher = AES.new(st.session_state.clave, AES.MODE_EAX)


if "texto_cifrado" not in st.session_state:
    # Inicializamos una variable para guardar el texto cifrado
    st.session_state.texto_cifrado = ""

# # Sección para subir un archivo de texto
archivo = st.file_uploader("Sube un archivo TXT", type=[
                           "txt"], key="file_uploader_1")


# Verificamos si el usuario ha subido un archivo
if archivo:
    # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    texto = archivo.read().decode()
    # Mostramos el contenido en un área de texto
    st.text_area("Contenido del archivo:", texto, height=200)

    # Botón para cifrar el texto
    if st.button("Cifrar"):
        
          # Cifrar
          cifrado, tag = st.session_state.cipher.encrypt_and_digest(texto.encode())
          st.markdown(
                f"**Texto a descifrar:** `{cifrado}`")
          
          st.session_state.texto_cifrado = cifrado
          st.markdown(
                f"**Texto a descifrar en sesion:** `{st.session_state.texto_cifrado}`")

            # Crea la carpeta si no existe
          if not os.path.exists("archivos"):
             os.makedirs("archivos")
         # Guardamos el texto cifrado en un archivo en la carpeta "archivos"
          with open("archivos/cifrado.txt", "wb") as f:
            f.write(st.session_state.texto_cifrado)

    #     st.success("Archivo cifrado guardado como 'archivos/cifrado.txt'")

    # Botón para descifrar el texto
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado:  # Verificamos si hay un texto cifrado guardado en la sesión
            st.markdown(
                f"**Texto a descifrar en session:** `{st.session_state.texto_cifrado}`")
           # Descifrar
            cipher_dec = AES.new(st.session_state.clave, AES.MODE_EAX, st.session_state.cipher.nonce)
            mensaje_descifrado = cipher_dec.decrypt(st.session_state.texto_cifrado ).decode()
            # Leer el contenido del archivo de texto
            with open("archivos/cifrado.txt", "rb") as txt_file:
                st.markdown(
                f"**Texto a descifrar en archivo:** `{txt_file.read()}`")

            # Guardamos el texto descifrado en un archivo dentro de la carpeta "archivos"
            with open("archivos/descifrado.txt", "w") as f:
                f.write(mensaje_descifrado)
            st.markdown(
                    f"**Texto a descifrado:** `{mensaje_descifrado}`")
            # Mensaje de confirmación de que el archivo ha sido guardado
            st.success(
                "Archivo descifrado guardado como 'archivos/descifrado.txt'")
        else:
            # Si no hay texto cifrado, mostramos una advertencia
            st.warning(
                "No hay un texto cifrado para descifrar. Cifra un texto primero.")
