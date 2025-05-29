import streamlit as st
import requests

# Set the app title
st.title('🌍 Travel Budget & Currency Exchange App')

# Add a welcome message
st.write('Welcome to the enhanced currency exchange and travel budget planner!')

# User input: custom message
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Input: Destination (place to go)
destination = st.text_input('Where do you want to go?', 'Japan')

# API call to get exchange rates
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data['rates']
    currency_list = sorted(rates.keys())  # Sorted for easier selection

    # Select the currency to convert from and to
    from_currency = st.selectbox('Convert from currency:', currency_list, index=currency_list.index("USD"))
    to_currency = st.selectbox('Convert to currency:', currency_list, index=currency_list.index("JPY"))

    # Input: Amount of money to convert
    amount = st.number_input('Enter amount of money to convert:', min_value=0.0, format="%.2f")

    # Calculate exchange rate
    if from_currency != 'USD':
        from_rate = rates[from_currency]
    else:
        from_rate = 1.0

    to_rate = rates[to_currency]

    # Convert amount
    if from_currency != to_currency:
        converted_amount = (amount / from_rate) * to_rate
    else:
        converted_amount = amount

    # Show results
    st.write(f"💼 Planning a trip to: **{destination}**")

