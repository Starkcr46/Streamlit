import streamlit as st
import pandas as pd

df = pd.read_csv("data/test.csv", dtype="int")
st.dataframe(df)
st.table(df)
st.metric(label="Population", value=900, delta=-20, delta_color="normal")
st.metric(label="Expenses", value=900, delta=-20, delta_color="inverse")