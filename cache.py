import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def create_list():
    l = [1,2,4]
    return l

l = create_list()
l.remove(1)

st.write(l)