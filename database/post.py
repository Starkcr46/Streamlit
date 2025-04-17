import streamlit as st
import pandas as pd
from supabase import create_client, Client

col1, col2, col3, col4 = st.columns(4)
length = col1.slider("Length", min_value=0, max_value=100, value=0, step=1)
width = col2.slider("Width", min_value=0, max_value=100, value=0, step=1)
height = col3.slider("Height", min_value=0, max_value=100, value=0, step=1)
message = col4.text_area("Message", height=200, placeholder="Write your message here")
index = -1
idVal = "none"


        

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

table_name = "reactTest"
rows = run_query(table_name)


def callback():
        index = st.session_state.df.selection.rows[0]
        idVal = rows.data[index]["id"]
        run_delete(table_name, idVal)

df = pd.json_normalize(rows.data)
#st.write(f"The table '{table_name}' has {row_count} rows.")
    #st.write(df)
st.dataframe(
        df,
        on_select=callback,
        selection_mode="single-row",
        key="df",
    )

def run_insert(table_name):
    return supabase.table(table_name).insert({"length": length, "width": width, "height": height, "message": message}).execute()

def run_delete(table_name, id):
    return supabase.table(table_name).delete().eq("id", id).execute()

def get_row_count(table_name):
    response = supabase.table(table_name).select("*", count="exact").execute()
    return len(response.data) if response.data else 0


row_count = get_row_count(table_name)


def onInsert():
    run_insert(table_name)
    #rows = run_query(table_name)
    #st.write("hello", rows.data[1]["id"])

#def onDelete():
#    run_delete(table_name)
   
    

st.button("Insert", on_click= onInsert)
#st.button("Delete", on_click= onDelete)
