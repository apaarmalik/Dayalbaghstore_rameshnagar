import streamlit as st
import pandas as pd
from PIL import Image
import os

# Set the desired working directory
custom_dir = "G:/Malik clothing & accessories"

os.chdir(custom_dir)
st.success(f"Working directory changed to: {os.getcwd()}")

st.write("hello")


fle = st.file_uploader("Upload the file",accept_multiple_files=True)

for f in fle:
  img=Image.open(f)
  st.image(img,caption='hi')


