import streamlit as st
import pandas as pd
from PIL import Image

st.write("hello")

img = Image.open('sample.png')
st.image(img, caption='Sunrise by the mountains')
