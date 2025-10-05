import streamlit as st
import pandas as pd
import random
import numpy
data=pd.read_csv("C:/Users/a/Documents/Employee.csv")

st.bar_chart(data)
st.line_chart(data)