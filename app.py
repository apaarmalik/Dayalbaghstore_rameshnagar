import streamlit as st
import pandas as pd
from PIL import Image

st.write("hello")

img = Image.open('D:/to/sample.png')
st.image(img, caption='Sunrise by the mountains')
