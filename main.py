from operator import index
import streamlit as st
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.title("Data Exploration and Analysis (EDA) Platform")
    choice = st.radio("Navigation", ["Upload","EDA"])
    st.info("Welcome to the Data Exploration and Analysis (EDA) Platform! This platform is designed to empower users  to  perform exploratory data analysis, and gain valuable insights from your datasets.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset (.csv files only)", ['csv'])
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "EDA": 
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)

