import streamlit as st 
import pandas as pd

st.title("Landlord Strategies")
property_price = st.number_input("Property price: ")
rent = st.number_input("Rent per month: ",step = 1)
taxes = st.number_input("Taxes per year: ",step = 1)
taxes_by_the_month = st.number_input("Taxes per month: ",taxes / 12)
maintenance = st.number_input("Maintenance per month: ")
profit_per_month = st.number_input("Profit per month: ",rent - (taxes_by_the_month + maintenance))
growthofrent = st.number_input(" Percent Growth rate increase in rent by year: ")
rent_per_year = st.number_input("Profit per year: ",profit_per_month * 12)
rentgrowthbyyear = st.slider("Rent growth per year: ",min_value = 1, max_value = 100)
profitgrowthbyyear = st.number_input("Profit growth per year: ",value = rent * (1+(rentgrowthbyyear/100)) - (taxes_by_the_month + maintenance))
