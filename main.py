import streamlit as st
import pandas as pd
import numpy

st.set_page_config(page_title="Random Data Explorer", layout="centered")

st.title("📊Random Data Explorer")

# Sidebar controls
st.sidebar.header("settings")
points = st.sidebar.slider("Number of data points", 10, 500, 100)
seed = st.sidebar.number_input("Random seed", value=42)
generate = st.sidebar.button("generate Data")

# Generate Data
if generate:
    np.random.seed(seed)
    data = {
        "x": np.linspace(0, 10, points),
        "y": np.sin(np.linspace(0, 10, points)) + np.random.normal(0, 0.5, points)
    }
    df = pd.DataFrame(data)
    
    st.success("✅ Data generated!")
    st.line_chart(df)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.info("👈 Use the sidebar to generate data.")