import streamlit as st
import pandas as pd
import openpyxl as px
import os
import io


file = st.file_uploader("Select an excel File", accept_multiple_files=False)
