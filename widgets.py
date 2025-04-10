import streamlit as st
import pandas as pd

primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Primary")
if secondary_btn:
    st.write("Secondary")

st.divider()

checkbox = st.checkbox("Checkbox")

if checkbox:
    st.write("Clicked")
else:
    st.write("Unclicked")

st.divider()

df = pd.read_csv("data/test.csv")

radio = st.radio("Choose an option", options = df.columns[1:], index=0, horizontal=False)

st.write(radio)

st.divider()

select = st.selectbox("Select an option", options = df.columns[1:], index=0)

st.write(select)

st.divider()

multiselect = st.multiselect("Choose multiple", options = df.columns[1:], default=["col1"], max_selections=3)

st.write(multiselect)

st.divider()

slider = st.slider("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(slider)

st.divider()

text_input = st.text_input("Write you name", placeholder="Chris Stark")

st.write(text_input)

st.divider()

num_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(num_input)

st.divider()

text_area = st.text_area("Tell me something", height=200, placeholder="Write your message here")

st.write(text_area)


