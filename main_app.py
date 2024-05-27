import streamlit as st
from file_loader import load_csv, load_excel, load_example_data
from data_cleaner import clean_data
from data_transformer import transform_data
from profiler import generate_profile_report
from download_helper import download_processed_data
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title="EDA App", layout="wide")

st.markdown("# EDA App")
st.markdown("### This app allows you to perform exploratory data analysis (EDA) on any dataset")

# Sidebar for file upload and example dataset
with st.sidebar.header('1. Upload your Dataset'):
    file_type = st.sidebar.selectbox("Choose file type", ["CSV", "Excel"])
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=["csv", "xlsx"])
    st.sidebar.markdown("""
    Example input file: 
    - Ensure it is a valid file of the selected type
    """)

if uploaded_file:
    if file_type == "CSV":
        df = load_csv(uploaded_file)
    elif file_type == "Excel":
        df = load_excel(uploaded_file)
    
    if df is not None:
        df = clean_data(df)
        df = transform_data(df)
        st.success("File uploaded and processed successfully!")
        pr = generate_profile_report(df)

        st.header("**Input Data Frame**")
        st.write(df.to_pandas())
        st.write("---")
        st.header("**Pandas Profiling Report**")
        st_profile_report(pr)

        if st.sidebar.button("Download Processed Data"):
            file_format = st.sidebar.selectbox("Select File Format", ["CSV", "Parquet"])
            buffer, format_type = download_processed_data(df, file_format)
            st.download_button(label="Download", data=buffer, file_name=f"processed_data.{format_type.lower()}")

else:
    st.info("Awaiting file to be uploaded. Alternatively, use the example dataset.")
    if st.button("Press to use example dataset"):
        df = load_example_data()
        pr = generate_profile_report(df)
        
        st.header("**Input Data Frame**")
        st.write(df.to_pandas())
        st.write("---")
        st.header("**Pandas Profiling Report**")
        st_profile_report(pr)
