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
destination = st.text_input('Where do you want to go?', '')

if destination.strip():  # Check if destination is not empty
    st.write(f"✈️ Planning a trip to: **{destination}**")

    # API call to get exchange rates
    response = requests.get('https://api.vatcomply.com/rates?base=USD')

    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        currency_list = sorted(rates.keys())

        # Select currencies
        from_currency = st.selectbox('Convert from currency:', currency_list, index=currency_list.index("USD"))
        to_currency = st.selectbox('Convert to currency:', currency_list, index=currency_list.index("JPY"))

        # Show amount input and calculate only if currencies are selected
        amount = st.number_input('Enter amount of money to convert:', min_value=0.0, format="%.2f")

        # Get exchange rates
        from_rate = rates[from_currency] if from_currency != 'USD' else 1.0
        to_rate = rates[to_currency]

        # Perform conversion
        converted_amount = (amount / from_rate) * to_rate if from_currency != to_currency else amount

        # Show results
        st.success(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

        # Optional: Show full exchange data
        with st.expander("Show full exchange rate data"):
            st.json(data)

    else:
        st.error(f"API call failed with status code: {response.status_code}")
else:
    st.warning("Please enter your destination to continue.")
