import streamlit as st
import pandas as pd

df = pd.read_csv("../data/student_performance.csv")

st.title("Student Performance Analytics")

st.dataframe(df.head())