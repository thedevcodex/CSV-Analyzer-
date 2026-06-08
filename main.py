import streamlit as st
import pandas as pd

st.title('CSV Analyzer 📊')
st.divider()
file=st.file_uploader("Upload Your File",type="csv",max_upload_size=2000)
if file :
    df = pd.read_csv(file)
    st.write("Columns , Rows Count",df.shape)
    st.subheader("Preview")
    st.dataframe(df.head(5))
    st.subheader('Column Names')
    st.dataframe(df.columns)
    st.subheader("Columns Data Type")
    st.dataframe(df.dtypes)
    st.subheader("Null Values Counts")
    st.dataframe(df.isnull().sum())
    st.subheader('Descriptive  Statistics')
    st.dataframe(df.describe(include='all'))
    st.subheader("Dataset")
    st.dataframe(df)
    st.divider()
    st.caption("Developed by TheDevCodex 💻")