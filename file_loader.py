import streamlit as st
import polars as pl
import pyarrow.csv as pv

@st.cache_data(ttl=3600)
def load_csv(file):
    try:
        table = pv.read_csv(file)
        csv = pl.from_arrow(table)
        return csv
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return None

@st.cache_data(ttl=3600)
def load_excel(file):
    try:
        df = pl.read_excel(file)
        return df
    except Exception as e:
        st.error(f"Error loading Excel: {e}")
        return None

@st.cache_data(ttl=3600)
def load_example_data():
    data = pl.DataFrame({
        'a': [1.0, 2.0, 3.0, 4.0, 5.0] * 20,
        'b': [2.0, 3.0, 4.0, 5.0, 6.0] * 20,
        'c': [3.0, 4.0, 5.0, 6.0, 7.0] * 20,
        'd': [4.0, 5.0, 6.0, 7.0, 8.0] * 20,
        'e': [5.0, 6.0, 7.0, 8.0, 9.0] * 20
    })
    return data
