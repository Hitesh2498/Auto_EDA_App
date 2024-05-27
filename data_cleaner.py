import streamlit as st
import polars as pl

def clean_data(df):
    st.sidebar.subheader("Data Cleaning Options")
    if st.sidebar.checkbox("Handle Missing Values"):
        fill_method = st.sidebar.selectbox("Fill with:", ["Mean", "Median", "Mode"])
        for col in df.columns:
            if df[col].null_count() > 0:
                if fill_method == "Mean":
                    df = df.with_columns(pl.col(col).fill_null(df[col].mean()).alias(col))
                elif fill_method == "Median":
                    df = df.with_columns(pl.col(col).fill_null(df[col].median()).alias(col))
                elif fill_method == "Mode":
                    mode_value = df[col].mode().to_list()[0]
                    df = df.with_columns(pl.col(col).fill_null(mode_value).alias(col))
    return df
