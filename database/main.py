import streamlit as st
import pandas as pd
from supabase import create_client, Client

@st.cache_resource
def init_connection():
    url: str = st.secrets['supabase_url']
    key: str = st.secrets['supabase_key']

    client: Client = create_client(url, key)

    return client


supabase = init_connection()

# Query the db


@st.cache_resource
def run_query(table_name):
    # Return all data
    return supabase.table(table_name).select("*").execute()

    # Filter data
    # return supabase.table('car_parts_monthly_sales').select("*").eq("parts_id", 2674).execute()

def get_row_count(table_name):
    response = supabase.table(table_name).select("*", count="exact").execute()
    return len(response.data) if response.data else 0

st.title("Query a database")

table_name = "car_parts_monthly_sales"
row_count = get_row_count(table_name)
st.write(f"The table '{table_name}' has {row_count} rows.")

rows = run_query(table_name)

# Store in dataframe
df = pd.json_normalize(rows.data)
st.write(df)