import streamlit as st
import pandas as pd
import Invalid_Data

st.title("Cab Data Analysis")
st.text("This webapp is for basic my-cab data analysis")

file = st.sidebar.file_uploader("Upload CSV file")
options = st.sidebar.radio('Pages',options=['Data','Statistics','Invalid Data'])

df = None

if file:
    with st.spinner("Reading File"):
        df = pd.read_csv(file)
        if options=='Data':
            st.write(df)
        elif options=='Statistics':
            st.write(df.describe())
        elif options=='Invalid Data':
            Invalid_Data.get_plot(df)

else:
    st.divider()
   
    st.warning("Please upload csv file to proceed")



