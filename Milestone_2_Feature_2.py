import os
import openai
import streamlit as st
from openai import OpenAI


st.markdown("# Flood Preparedness Assistant")
st.sidebar.markdown("# Flood Preparedness Assistant")

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()


# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "You are a flood preparedness expert. Provide concise, actionable advice on flood prevention, safety, \
                         equipment, and preparation. Answer questions with practical tips and specific recommendations. Make sure to display the questions in bullet point format and provide how each bullet point and a brief description of each point in sub bullet point format. Also display phone numbers to call in case of a flood for each response like first responders in San Jose"},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_input("Provide questions about flood information (e.g., equipment to use to protect my house from flooding?):") 
    
    submitted = st.form_submit_button("Generate Tips")
    
    if submitted:
        st.write(get_completion(prompt))
