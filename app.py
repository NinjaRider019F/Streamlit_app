# import liberaries:-
import pandas as pd
import streamlit as st
import seaborn as sns                                                                                                                                                                                                           

# Title and Sub header:-
st.title("Pandas Data Analysis with Streamlit")
st.subheader("Data Analysis using Pandas and Streamlit")
st.text("This is a simple data analysis app using Pandas and Streamlit.")       

# Upload dataset:-
upload = st.file_uploader("Upload CSV file", type=["csv"])
if upload is not None:
    data = pd.read_csv(upload)

# Show dataset:-
if upload is not None:
    if st.checkbox("Preview dataset: "):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())  # Will show last 5 rows of the dataset

# Check datatype of each column:-
if upload is not None:
    if st.checkbox("Check datatype of each column: "):
        st.text("Data types of each column: ")
        st.write(data.dtypes)

# Find shape of dataset (Number of rows and columns) :-
if upload is not None:
    data_shape=st.radio("what shape of dataset you want to see?",("Rows","Columns","Both"))
    if data_shape=="Rows":
        st.write(data.shape[0])  # Will show number of rows
    if data_shape=="Columns":
        st.write(data.shape[1])  # Will show number of columns
    if data_shape=="Both":
        st.write(data.shape)  # Will show number of rows and columns

# Find null values in the dataset:-
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null values in the dataset: "):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("No null values in the dataset")

 # Find duplicate values in the dataset:- 

if upload is not None:
    test= data.duplicated().any()
    if test==True:
        st.warning("Duplicate values are present in the dataset")
        dup=st.selectbox("Do you want to remove duplicate values?",("Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate values removed successfully")
            st.write(data)
        if dup=="No":
            st.text("Duplicate values are not removed")
    else:
        st.success("No duplicate values in the dataset")

# Get overall statistics of the dataset:-
if upload is not None:
    if st.checkbox("Summary of the dataset: "):
        st.write(data.describe(include='all')) # include='all' will show statistics of all columns including categorical columns

# About section:- 
if st.button("About"):
    st.text("Built with Streamlit")
    st.text("Created by Jatin Sharma")
    st.text("Version 1.0.0")
    st.text("This is a simple data analysis app using Pandas and Streamlit.")

# By contact section:- 
if st.button("Contact Me"):
    st.text("Email: jjaatinsharma123@gmail.com")

