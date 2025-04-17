import streamlit as st
import pandas as pd
from supabase import create_client, Client

col1, col2, col3, col4 = st.columns(4)
length = col1.slider("Length", min_value=0, max_value=100, value=0, step=1)
width = col2.slider("Width", min_value=0, max_value=100, value=0, step=1)
height = col3.slider("Height", min_value=0, max_value=100, value=0, step=1)
message = col4.text_area("Message", height=200, placeholder="Write your message here")

@st.cache_resource
def init_connection():
    url: str = st.secrets['supabase_url']
    key: str = st.secrets['supabase_key']

    client: Client = create_client(url, key)

    return client

supabase = init_connection()

def run_query(table_name):
    # Return all data
    return supabase.table(table_name).select("*").execute()

def run_insert(table_name):
    # Return all data
    return supabase.table(table_name).insert({"length": length, "width": width, "height": height, "message": message}).execute()

def get_row_count(table_name):
    response = supabase.table(table_name).select("*", count="exact").execute()
    return len(response.data) if response.data else 0

table_name = "reactTest"
row_count = get_row_count(table_name)


def onSearch():
    run_insert(table_name)
    rows = run_query(table_name)
    df = pd.json_normalize(rows.data)
    st.write(f"The table '{table_name}' has {row_count} rows.")
    st.write(df)
 
st.button("Insert", on_click= onSearch)
