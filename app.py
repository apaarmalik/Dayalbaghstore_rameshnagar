import streamlit as st
import pandas as pd
from PIL import Image
import os
import glob

# Title

img_files=glob.glob("newsubfolder./*.png")
sorted_list=img_files.sort()
for imgs in sorted_list:
  st.write(imgs)



