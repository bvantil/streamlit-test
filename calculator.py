import streamlit as st

# Title of the app
st.title('Custom Pricing Calculator')

# User inputs
user_age = st.text_input('Enter your age:', '25')
user_location = st.text_input('Enter your location:', 'New York')

# Button to calculate pricing
if st.button('Calculate Pricing'):
    # Simple pricing logic based on age
    base_price = 100
    age_discount = max(0, (40 - int(user_age)) * 2)
    customized_price = base_price - age_discount

    # Display the result
    st.write(f'Your custom price is: ${customized_price}')

# Run this with `streamlit run this_script.py`
