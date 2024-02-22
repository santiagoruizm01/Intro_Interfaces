import streamlit as st
from PIL import Image

st.title(" Aplicación INTERFACES ")

st.header(" En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write(" Fácilmente puedo realizar backend y frontend")
image = Image.open('Gaming.jpg')

st.image(image, caption='Interfaces multimodales')
