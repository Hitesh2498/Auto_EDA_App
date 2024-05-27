import streamlit as st
import polars as pl

def transform_data(df):
    st.sidebar.subheader("Data Transformation Options")
    if st.sidebar.checkbox("Scale Data"):
        numeric_cols = df.select(pl.col(pl.Float64)).columns + df.select(pl.col(pl.Int64)).columns
        selected_scale_cols = st.sidebar.multiselect("Select columns to scale", numeric_cols)
        scaler = st.sidebar.selectbox("Scaling Method", ["StandardScaler", "MinMaxScaler"])
        if scaler == "StandardScaler":
            for col in selected_scale_cols:
                df = df.with_columns(((pl.col(col) - pl.col(col).mean()) / pl.col(col).std()).alias(col))
        elif scaler == "MinMaxScaler":
            for col in selected_scale_cols:
                df = df.with_columns(((pl.col(col) - pl.col(col).min()) / (pl.col(col).max() - pl.col(col).min())).alias(col))
    if st.sidebar.checkbox("Encode Categorical Variables"):
        categorical_cols = df.select(pl.col(pl.Utf8)).columns
        selected_encode_cols = st.sidebar.multiselect("Select columns to encode", categorical_cols)
        for col in selected_encode_cols:
            dummies = df.select(pl.col(col)).to_dummies()
            df = df.drop(col).hstack(dummies)
    return df
