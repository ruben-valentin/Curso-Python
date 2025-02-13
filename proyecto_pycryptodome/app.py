# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema
# Importamos las funciones de cifrado y descifrado
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generar clave y vector de inicialización (IV)
clave = get_random_bytes(16)
cipher = AES.new(clave, AES.MODE_EAX)

# Título de la aplicación en la interfaz de Streamlit
st.title("Cifrado Pycryptodome - Codificación y Decodificación")

# Inicializar variables de sesión en Streamlit para mantener el estado entre interacciones

if "texto_cifrado" not in st.session_state:
    # Inicializamos una variable para guardar el texto cifrado
    st.session_state.texto_cifrado = ""

# # Sección para subir un archivo de texto
archivo = st.file_uploader("Sube un archivo TXT", type=[
                           "txt"], key="file_uploader_1")

# Verificamos si el usuario ha subido un archivo
if archivo:
    # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    texto = archivo.read().decode("utf-8")
    # Mostramos el contenido en un área de texto
    st.text_area("Contenido del archivo:", texto, height=200)

    # Botón para cifrar el texto
    if st.button("Cifrar"):
        # Aplicamos el cifrado César con el desplazamiento seleccionado y guardamos el resultado en la sesión
        cifrado, tag = cipher.encrypt_and_digest(texto.encode())
        st.session_state.texto_cifrado = cifrado
        # cifrar_cesar(texto, st.session_state.desplazamiento)
        st.text_area("Texto Cifrado:", st.session_state.texto_cifrado,
                     height=200)  # Mostramos el texto cifrado

        # Verificar si el directorio "archivos" existe, si no, crearlo
        if not os.path.exists("archivos"):
            os.makedirs("archivos")

        # Guardamos el texto cifrado en un archivo en la carpeta "archivos"
        # with open("archivos/cifrado.txt", "w") as f:
        #     # el texto cifrado es una tupla por eso cogemos el valor de la primera posicion y convierte en hexadecimal
        #     f.write(st.session_state.texto_cifrado.hex())

        # Mensaje de confirmación de que el archivo ha sido guardado
        st.success("Archivo cifrado guardado como 'archivos/cifrado.txt'")

    # Botón para descifrar el texto
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado:  # Verificamos si hay un texto cifrado guardado en la sesión

            cipher_dec = AES.new(clave, AES.MODE_EAX, cipher.nonce)

            # el mensaje antes de descifrarlo, se debe  convertir de nuevo a bytes:
            # Convertir de hexadecimal a bytes
            # Convertir a str y luego a bytes
            # ciphertext = bytes.fromhex(
            #     st.session_state.texto_cifrado[0].decode())
            st.markdown(
                f"**Texto a descifrar:** `{st.session_state.texto_cifrado}`")
            texto_descifrado = cipher_dec.decrypt(
                st.session_state.texto_cifrado)
            # Mostramos información adicional sobre el texto a descifrar
            st.markdown(
                f"**Texto a descifrar:** `{st.session_state.texto_cifrado}`")

            st.text_area("Texto Descifrado:", texto_descifrado.decode(),
                         height=200)  # Mostramos el texto descifrado

            # Guardamos el texto descifrado en un archivo dentro de la carpeta "archivos"
            with open("archivos/descifrado.txt", "w") as f:
                f.write(texto_descifrado)

            # Mensaje de confirmación de que el archivo ha sido guardado
            st.success(
                "Archivo descifrado guardado como 'archivos/descifrado.txt'")
        else:
            # Si no hay texto cifrado, mostramos una advertencia
            st.warning(
                "No hay un texto cifrado para descifrar. Cifra un texto primero.")
