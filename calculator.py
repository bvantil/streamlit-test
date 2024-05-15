import streamlit as st
import math

# Title of the app
st.title('Custom Contract Pricing Calculator')

# User inputs using sliders
company_name = st.text_input('Enter your company name:')
annual_revenue = st.slider('Select your annual revenue (USD):', min_value=10000000, max_value=10000000000, step=10000000, format='$%d')
annual_contract_volume = st.slider('Select your annual number of contracts:', min_value=10, max_value=1000, step=10)
average_pages_per_contract = st.slider('Select average pages per contract:', min_value=10, max_value=250, step=25)

# Button to calculate pricing
if st.button('Calculate Pricing'):
    # Calculation of Base Fee using log regression
    fee_percent = -0.0000194472 * math.log(annual_revenue) + 0.0004408921
    base_fee = annual_revenue * fee_percent
    
    # PLL Costs and Variable Costs
    pll_costs = base_fee * 0.20
    variable_costs = base_fee * 0.39 * (annual_contract_volume * average_pages_per_contract * 0.001)

    # Foundation Fee calculation
    foundation_fee = base_fee + pll_costs + variable_costs

    # Calculating further tiers
    framework_fee = foundation_fee * 1.4
    pinnacle_fee = framework_fee * 1.4

    # Display the formatted results
    st.write(f'Thank you for your interest in Contract Manager, {company_name}. Your custom pricing is as follows:')
    st.write(f'Foundation Tier annual pricing is: ${foundation_fee:.2f}')
    st.write(f'Framework Tier annual pricing is: ${framework_fee:.2f}')
    st.write(f'Pinnacle Tier annual pricing is: ${pinnacle_fee:.2f}')

# Run this with `streamlit run this_script.py`

