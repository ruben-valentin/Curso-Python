import streamlit as st
import os
from cesar import cifrar_cesar, descifrar_cesar

st.title("Cifrado César - Codificación y Decodificación")

# Inicializar sesión para guardar datos
if "desplazamiento" not in st.session_state:
    st.session_state.desplazamiento = 3  # Valor por defecto
if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Para guardar el texto cifrado

# Subir archivo
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_1")

if archivo:
    texto = archivo.read().decode("utf-8")  # Leer el contenido del archivo
    st.text_area("Contenido del archivo:", texto, height=200)

    # Usamos un slider con sesión de estado para recordar el desplazamiento
    desplazamiento = st.slider("Selecciona el desplazamiento", 1, 27, st.session_state.desplazamiento)
    st.session_state.desplazamiento = desplazamiento  # Guardamos el valor

    # Botón para cifrar
    if st.button("Cifrar"):
        st.session_state.texto_cifrado = cifrar_cesar(texto, st.session_state.desplazamiento)
        st.text_area("Texto Cifrado:", st.session_state.texto_cifrado, height=200)
        
        with open("archivos/cifrado.txt", "w") as f:
            f.write(st.session_state.texto_cifrado)
        st.success("Archivo cifrado guardado como 'archivos/cifrado.txt'")

    # Botón para descifrar
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado:  # Verificamos si hay un texto cifrado
            texto_descifrado = descifrar_cesar(st.session_state.texto_cifrado, st.session_state.desplazamiento)
            
            st.markdown(f"**Texto a descifrar:** `{st.session_state.texto_cifrado}`")
            st.markdown(f"**Desplazamiento aplicado:** `{st.session_state.desplazamiento}`")
            st.text_area("Texto Descifrado:", texto_descifrado, height=200)

            with open("archivos/descifrado.txt", "w") as f:
                f.write(texto_descifrado)
            st.success("Archivo descifrado guardado como 'archivos/descifrado.txt'")
        else:
            st.warning("No hay un texto cifrado para descifrar. Cifra un texto primero.")
