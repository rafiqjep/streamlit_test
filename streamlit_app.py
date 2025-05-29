import streamlit as st 
import requests

# Page configuration
st.set_page_config(page_title="Currency Exchange", page_icon="💱", layout="centered")

# Display logo (replace with your own path or URL)
st.image("https://cdn-icons-png.flaticon.com/512/263/263115.png", width=100)  # Example logo

# App title and welcome message
st.markdown("<h1 style='text-align: center; color: navy;'>🌍 Choose Your Currency</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Welcome to the <strong>Currency Exchange App</strong>!</p>", unsafe_allow_html=True)
st.write("")

# Custom message input
widgetuser_input = st.text_input('✏️ Enter a custom message:', 'Hello, Streamlit!') 
st.info(f'📝 Customized Message: {widgetuser_input}')

# Fetch exchange rates
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data['rates']

    # Dropdown to select currency
    currency_list = sorted(rates.keys())
    selected_currency = st.selectbox('💱 Choose a currency to see the exchange rate:', currency_list)

    # Display selected exchange rate
    exchange_rate = rates[selected_currency]
    st.success(f"💵 1 USD = {exchange_rate} {selected_currency}")

    # Show full JSON response in an expander
    with st.expander("📦 Show full exchange rate data"):
        st.json(data)

else:
    st.error(f"❌ API call failed with status code: {response.status_code}")
