import streamlit as st
import pandas as pd
from PIL import Image
import os
import glob
from streamlit_sortables import sort_items

# Title

img_files=glob.glob("newsubfolder./*.png")
sorted_images=sort_items(img_files)
for imgs in img_files:
  st.image(imgs, caption = imgs)



