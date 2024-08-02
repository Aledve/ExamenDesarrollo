import streamlit as st
import requests

st.title("Clasificador de Textos") #Titulo de la pp
codigo = st.number_input("codigo", min_value=1)
valor = st.text_area("Texto")

if st.button("Clasificar"):
    response = requests.post("http://localhost:8008/clasificar/", json={'codigo':codigo, 'valor':valor})
    respuesta = response.json()
    st.write(f"Código: {respuesta['codigo']}, Respuesta:{respuesta['respuesta']}")

    if "historial" not in st.session_state:st.session_state.historial =[]
    st.session_state.historial.append(respuesta)
    st.write("Historial de respuestas:")
    for item in st.session_state.historial:st.write(item)



