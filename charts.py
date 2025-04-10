import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/test.csv")
st.line_chart(df, x="year", y=["col1", "col2", "col3"])
st.area_chart(df, x="year", y=["col1", "col2", "col3"])
st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

geo = pd.read_csv("data/coords.csv")
st.map(geo)
fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title("My title")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate()
st.pyplot(fig)