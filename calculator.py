import streamlit as st

# Title of the app
st.title('Custom Pricing Calculator for Contract Manager')

# User inputs
company_name = st.text_input('Enter your company name:')
annual_revenue = st.number_input('Enter your annual revenue (USD):', min_value=0.0, format='%f')
annual_contract_volume = st.number_input('Enter your annual contract volume:', min_value=0, format='%d')
average_pages_per_contract = st.number_input('Enter average pages per contract:', min_value=0, format='%d')

# Button to calculate pricing
if st.button('Calculate Pricing'):
    # Pricing logic based on the inputs
    # Example: Simple multiplier for demonstration purposes
    base_price = 500  # Base price for calculation
    revenue_factor = annual_revenue / 1000000  # Small revenue factor
    volume_discount = max(0, (100 - annual_contract_volume) * 0.5)  # Volume discount
    pages_factor = average_pages_per_contract * 2  # Cost factor per page

    # Calculating final price
    customized_price = base_price + revenue_factor - volume_discount + pages_factor

    # Display the result
    st.write(f'{company_name}, your custom price is: ${customized_price:.2f}')

# Run this with `streamlit run this_script.py`
