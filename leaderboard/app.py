import streamlit as st
import pandas as pd

st.title(" Graph Robustness Leaderboard")

df = pd.read_csv("leaderboard/leaderboard.csv")

st.dataframe(df, use_container_width=True)
