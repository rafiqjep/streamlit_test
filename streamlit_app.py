import streamlit as st
import pandas as pd

# Set the app title
st.title('Halal E-number Checker 🕌')

# Add a welcome message
st.write('Check if an E-number is Halal, Haram, or Doubtful.')

# Load E-number data from a CSV file (make sure e_numbers.csv is in the same folder)
@st.cache_data
def load_data():
    return pd.read_csv('e_numbers.csv')

data = load_data()

# User input
e_number_input = st.text_input('Enter an E-number (e.g., E120):', '')

# Process input
if e_number_input:
    e_number_input = e_number_input.strip().upper()
    result = data[data['e_number'] == e_number_input]
    
    if not result.empty:
        status = result.iloc[0]['status']
        description = result.iloc[0]['description']
        st.success(f"**{e_number_input} is {status}**")
        st.info(f"**Description:** {description}")
    else:
        st.warning("E-number not found in the database.")

# Optional: display the full list
with st.expander("Show all E-numbers"):
    st.dataframe(data)
