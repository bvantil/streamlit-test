import streamlit as st
import math

# Custom styles for the app
st.markdown("""
<style>
    /* Base styles */
    .css-1xi51a1 {
        font-size: 18px;
    }
    .css-1cpxqw2 {
        font-size: 20px;  /* Bigger text on slider labels */
    }
    .st-bf {  /* This targets the slider handle */
        background-color: #02006c !important;
    }
    .st-eq {  /* This targets the slider track */
        background-color: #ccd6f6 !important;
    }
    .stSlider .css-14f6t7n {  /* This targets the overall slider component */
        height: 36px;
        padding: 10px 0;  /* Bigger sliders for easier interaction */
    }
    .stSlider .css-14f6t7n .css-1cpxqw2 {
        font-size: 16px;  /* Bigger and more readable slider labels */
    }
    /* Bold only the dollar amounts in the output */
    .pricing-output {
        font-size: 24px;
        font-weight: normal;
    }
    .pricing-output .dollar {
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title of the app
st.title('Custom Contract Pricing Calculator')

# User inputs using sliders
company_name = st.text_input('Enter your company name:')
annual_revenue = st.slider('Select your annual revenue (USD):', min_value=10000000, max_value=1000000000, step=10000000, format='$%d')
annual_contract_volume = st.slider('Select your annual number of contracts:', min_value=10, max_value=500, step=20)
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
    st.markdown(f'Thank you for your interest in Contract Manager. Based on the inputs you\'ve provided, a ballpark estimate for use in {company_name} is:', unsafe_allow_html=True)
    st.markdown(f'<div class="pricing-output">Foundation Tier annual pricing is: <span class="dollar">${foundation_fee:,.2f}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pricing-output">Framework Tier annual pricing is: <span class="dollar">${framework_fee:,.2f}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pricing-output">Pinnacle Tier annual pricing is: <span class="dollar">${pinnacle_fee:,.2f}</span></div>', unsafe_allow_html=True)

# Run this with `streamlit run this_script.py`
