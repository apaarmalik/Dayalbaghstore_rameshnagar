import streamlit as st
import pandas as pd
from PIL import Image

st.write("hello")

img=st.file_uploader("Upload the file",accept_multiple_files=False)

st.image(img, caption='Sunrise by the mountains')
