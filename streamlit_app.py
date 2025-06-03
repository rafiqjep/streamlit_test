import streamlit as st
import pandas as pd

# Load the E-number data
data = pd.read_csv("e_numbers.csv")

st.title("Halal E-Number Checker")

# Input from user
e_input = st.text_input("Enter E-number (e.g., E120)").upper()

if e_input:
    result = data[data['e_number'] == e_input]
    if not result.empty:
        status = result.iloc[0]['status']
        description = result.iloc[0]['description']
        st.write(f"**Status:** {status}")
        st.write(f"**Description:** {description}")
    else:
        st.warning("E-number not found in the database.")
