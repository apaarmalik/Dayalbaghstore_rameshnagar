import streamlit as st
import pandas as pd
from PIL import Image
import os
from pathlib import Path

# Title
st.title("Display Images from a Local Folder")

# Define the folder containing images
image_folder = Path("G:/Malik clothing & accessories")

# Check if folder exists
if not image_folder.exists():
    st.error(f"Folder not found: {image_folder}")
else:
    # Get a list of image files (filtering for common image formats)
    image_files = list(image_folder.glob("*.png")) + list(image_folder.glob("*.jpg")) + list(image_folder.glob("*.jpeg")) + list(image_folder.glob("*.gif"))

    # If no images found, display a message
    if not image_files:
        st.warning("No images found in the specified folder.")
    else:
        for image_file in image_files:
            st.image(image_file, caption=image_file.name, use_column_width=True)




# Set the desired working directory
custom_dir = "G:/Malik clothing & accessories"

os.chdir(custom_dir)
st.success(f"Working directory changed to: {os.getcwd()}")

st.write("hello")


fle = st.file_uploader("Upload the file",accept_multiple_files=True)

for f in fle:
  img=Image.open(f)
  st.image(img,caption='hi')


