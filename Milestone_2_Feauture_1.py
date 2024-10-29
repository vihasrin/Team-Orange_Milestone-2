import streamlit as st
import os
import openai
from openai import OpenAI
from pathlib import Path
import pandas as pd


st.title('Flood Hazard Zones in San Jose')
st.markdown('This map provides a general concentration of flooding hotspots in the greater San Jose region.')
df = pd.read_csv("/Users/harshilpurohit/Desktop/Projects/118i-tutorial/Flood_Data_Map_v1.csv")

# If your latitude and longitude columns are named differently, rename them
df = df.rename(columns={"your_lat_column": "lat", "your_lon_column": "lon"})

# Display the DataFrame on a map
st.map(df)
