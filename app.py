import streamlit as st
import pandas as pd
from PIL import Image

st.write("hello")


st.image(f'D:\\sample.png', caption='Sunrise by the mountains')

fle = st.file_uploader("Upload the file",accept_multiple_files=True)

for f in fle:
  img=Image.open(f)
  st.image(img,caption='hi')


