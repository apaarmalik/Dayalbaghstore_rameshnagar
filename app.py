import streamlit as st
import pandas as pd
from PIL import Image
import os
import glob

# Title
st.image("G:\pullover1.png")

img_files=glob.glob("G:\Malik clothing & accessories\*.png")
st.write(len(img_files))



