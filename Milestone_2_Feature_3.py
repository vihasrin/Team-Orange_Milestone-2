import streamlit as st

# Streamlit app title
st.title("Flood Reporting Form")

# Input form for flood report
with st.form(key="flood_report"):
    address = st.text_input("Enter the street address:")
    time = st.time_input("Enter the time of the flood observation:")
    day = st.selectbox("Select the day of the observation:", 
                       ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    severity = st.slider("Rate the flood severity (1-10):", 1, 10, 1)

    submitted = st.form_submit_button("Submit Report")

    if submitted:
        # Display the submitted report
        st.success("Flood report submitted successfully!")
        st.write("### Submitted Flood Report")
        st.write(f"**Address:** {address}")
        st.write(f"**Time:** {time.strftime('%H:%M')}")
        st.write(f"**Day:** {day}")
        st.write(f"**Severity:** {severity}/10")  

    
