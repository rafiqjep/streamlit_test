import streamlit as st
import csv

# Set the app title
st.title('Halal E-number Checker 🕌')

# Add a welcome message
st.write('Check if an E-number is Halal, Haram, or Doubtful.')

# Load data from CSV without using pandas
@st.cache_data
def load_data():
    e_list = []
    try:
        with open('e_numbers.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                e_list.append({
                    'e_number': row['e_number'].strip().upper(),
                    'status': row['status'].strip(),
                    'description': row['description'].strip()
                })
    except FileNotFoundError:
        st.error("The file 'e_numbers.csv' was not found.")
    return e_list

data = load_data()

# User input
e_input = st.text_input("Enter an E-number (e.g., E120):", "").strip().upper()

# Search for the E-number
if e_input:
    found = False
    for item in data:
        if item['e_number'] == e_input:
            st.success(f"**{e_input} is {item['status']}**")
            st.info(f"**Description:** {item['description']}")
            found = True
            break
    if not found:
        st.warning("E-number not found in the database.")
