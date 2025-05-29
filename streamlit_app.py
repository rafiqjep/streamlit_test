import streamlit as st 
import requests

# Set the app title 
st.title('💱 Currency Exchange Rate Viewer') 

# Add a welcome message 
st.write('Welcome to the currency exchange app!')

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# API call to get exchange rates
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data['rates']

    # Create a dropdown to select currency
    currency_list = sorted(rates.keys())  # Sort for easier navigation
    selected_currency = st.selectbox('Choose a currency to see the exchange rate:', currency_list)

    # Show the exchange rate
    exchange_rate = rates[selected_currency]
    st.success(f"1 USD = {exchange_rate} {selected_currency}")

    # Optionally show full JSON
    with st.expander("Show full exchange rate data"):
        st.json(data)

else:
    st.error(f"API call failed with status code: {response.status_code}")
