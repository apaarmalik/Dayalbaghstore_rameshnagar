import streamlit as st
import pandas as pd
from PIL import Image
import os
import glob

# Title

img_files=glob.glob("G://Malik clothing & accessories//*//*.PNG")
st.write(len(img_files))



