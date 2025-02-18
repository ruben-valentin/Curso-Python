# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Título de la aplicación
st.title("Cifrado Pycryptodome - Codificación y Decodificación")

# Inicializar variables de sesión en Streamlit para mantener el estado entre interacciones
if "clave" not in st.session_state:
    st.session_state.clave = get_random_bytes(16)  # Generar clave AES de 16 bytes

if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = None  # Inicializamos la variable del texto cifrado

if "nonce" not in st.session_state:
    st.session_state.nonce = None  # Inicializar nonce

if "tag" not in st.session_state:
    st.session_state.tag = None  # Inicializar el tag

# Sección para subir un archivo de texto
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_1")

# Verificamos si el usuario ha subido un archivo
if archivo:
    # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    texto = archivo.read().decode()
    st.text_area("Contenido del archivo:", texto, height=200)

    # Botón para cifrar el texto
    if st.button("Cifrar"):
        # Generar un nuevo objeto cipher en cada cifrado
        cipher = AES.new(st.session_state.clave, AES.MODE_EAX)
        
        # Cifrar el texto
        cifrado, tag = cipher.encrypt_and_digest(texto.encode())

        # Guardar en session_state
        st.session_state.texto_cifrado = cifrado
        st.session_state.nonce = cipher.nonce
        st.session_state.tag = tag  # Guardamos el tag para verificar autenticidad

        # Mostrar texto cifrado
        st.markdown(f"**Texto cifrado:** `{cifrado}`")

        # Crea la carpeta si no existe
        if not os.path.exists("archivos"):
            os.makedirs("archivos")

        # Guardamos el texto cifrado en un archivo dentro de la carpeta "archivos"
        with open("archivos/cifrado.txt", "wb") as f:
            f.write(cifrado)

        st.success("Archivo cifrado guardado como 'archivos/cifrado.txt'")

    # Botón para descifrar el texto
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado and st.session_state.nonce and st.session_state.tag:
            # Crear el cipher con los valores guardados
            cipher_dec = AES.new(st.session_state.clave, AES.MODE_EAX, nonce=st.session_state.nonce)

            try:
                # Descifrar y verificar
                mensaje_descifrado = cipher_dec.decrypt_and_verify(st.session_state.texto_cifrado, st.session_state.tag).decode()

                # Guardamos el texto descifrado en un archivo dentro de la carpeta "archivos"
                with open("archivos/descifrado.txt", "w") as f:
                    f.write(mensaje_descifrado)

                # Mostrar el mensaje descifrado
                st.markdown(f"**Texto descifrado:** `{mensaje_descifrado}`")
                st.success("Archivo descifrado guardado como 'archivos/descifrado.txt'")

            except ValueError:
                st.error("Error: El texto cifrado no es válido o la clave es incorrecta.")
        else:
            st.warning("No hay un texto cifrado válido para descifrar. Cifra un texto primero.")
