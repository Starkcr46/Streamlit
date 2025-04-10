from datetime import timedelta
import streamlit as st
import pandas as pd

with st.sidebar:
    st.write("Text in sidebar")

col1, col2, col3 = st.columns(3)
col1.write("Column1")
slider = col2.slider("Pick a number", min_value=0, max_value=10, value=0, step=1)
col3.checkbox("Column3")
df = pd.read_csv("data/test.csv", dtype="int")
tab1, tab2 = st.tabs(["Line Plot", "Bar Plot"])
with tab1:
    tab1.write("Line Plot")
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])

with tab2:
    tab2.write("Bar Plot")
    st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

with st.expander("Click to Expand"):
    st.image("data/hello.jpeg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)

with st.container():
    st.write("This is inside the container")

st.write("This is outside the container")

with st.form("form_key"):
    st.write("What would you like to order?")

    app = st.selectbox(label="Appetizers", options=["option1", "option2", "option3"])

    main = st.selectbox(label="Main Course", options=["option1", "option2", "option3"])

    dessert = st.selectbox(label="Dessert", options=["option1", "option2", "option3"])

    wine = st.checkbox(label="Are you bringing your own wine?")

    date = st.date_input(label="When are you coming?", value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False, label_visibility="visible")

    time = st.time_input(label="What time are you coming?", value="now", key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", step=timedelta(minutes=15))

    area = st.text_area("Any allergies?", height=200, placeholder="None")

    submit_button = st.form_submit_button(label="Submit", help=None, on_click=None, args=None, kwargs=None, type="secondary", icon=None, disabled=False, use_container_width=False)

    if submit_button:
        st.write(f""" Order Summary 
                 
        Appetizer: {app}

        Main Course: {main}

        Dessert: {dessert}

        Are you bringing your own wine? {"yes" if wine else "no"}
        
        Date of Visit: {date}

        Time of Visit: {time}
        
        Allergies: {area}
        
        """)
        
