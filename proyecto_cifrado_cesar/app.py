# Importamos las bibliotecas necesarias
import streamlit as st  # Streamlit para crear la interfaz web
import os  # Módulo para manejar archivos en el sistema
from cesar import cifrar_cesar, descifrar_cesar  # Importamos las funciones de cifrado y descifrado

# Título de la aplicación en la interfaz de Streamlit
st.title("Cifrado César - Codificación y Decodificación")

# Inicializar variables de sesión en Streamlit para mantener el estado entre interacciones
if "desplazamiento" not in st.session_state:
    st.session_state.desplazamiento = 3  # Asignamos un valor por defecto de desplazamiento

if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

# Sección para subir un archivo de texto
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_1")

# Verificamos si el usuario ha subido un archivo
if archivo:
    texto = archivo.read().decode("utf-8")  # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    st.text_area("Contenido del archivo:", texto, height=200)  # Mostramos el contenido en un área de texto

    # Slider para seleccionar el desplazamiento, recordando el valor en la sesión
    desplazamiento = st.slider("Selecciona el desplazamiento", 1, 27, st.session_state.desplazamiento)
    st.session_state.desplazamiento = desplazamiento  # Guardamos el valor del desplazamiento en la sesión

    # Botón para cifrar el texto
    if st.button("Cifrar"):
        # Aplicamos el cifrado César con el desplazamiento seleccionado y guardamos el resultado en la sesión
        st.session_state.texto_cifrado = cifrar_cesar(texto, st.session_state.desplazamiento)
        st.text_area("Texto Cifrado:", st.session_state.texto_cifrado, height=200)  # Mostramos el texto cifrado

        # Guardamos el texto cifrado en un archivo en la carpeta "archivos"
        with open("archivos/cifrado.txt", "w") as f:
            f.write(st.session_state.texto_cifrado)

        # Mensaje de confirmación de que el archivo ha sido guardado
        st.success("Archivo cifrado guardado como 'archivos/cifrado.txt'")

    # Botón para descifrar el texto
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado:  # Verificamos si hay un texto cifrado guardado en la sesión
            texto_descifrado = descifrar_cesar(st.session_state.texto_cifrado, st.session_state.desplazamiento)
            
            # Mostramos información adicional sobre el texto a descifrar
            st.markdown(f"**Texto a descifrar:** `{st.session_state.texto_cifrado}`")
            st.markdown(f"**Desplazamiento aplicado:** `{st.session_state.desplazamiento}`")

            st.text_area("Texto Descifrado:", texto_descifrado, height=200)  # Mostramos el texto descifrado

            # Guardamos el texto descifrado en un archivo dentro de la carpeta "archivos"
            with open("archivos/descifrado.txt", "w") as f:
                f.write(texto_descifrado)

            # Mensaje de confirmación de que el archivo ha sido guardado
            st.success("Archivo descifrado guardado como 'archivos/descifrado.txt'")
        else:
            # Si no hay texto cifrado, mostramos una advertencia
            st.warning("No hay un texto cifrado para descifrar. Cifra un texto primero.")
