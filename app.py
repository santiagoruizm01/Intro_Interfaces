import streamlit as st
from PIL import Image

st.title(" Aplicación INTERFACES ")

st.header(" En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write(" Fácilmente puedo realizar backend y frontend")
image = Image.open('Gaming.jpg')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('CORRECTO')

