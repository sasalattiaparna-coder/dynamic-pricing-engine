import streamlit as st 
from pricing import dynamic_price
from utils import get_competitor_price

st.title("🛒 Dynamic Pricing Engine")

demand = st.slider("Demand", 0, 100, 50)
inventory = st.slider("Inventory", 0, 200, 50)
season = st.selectbox("Season", [0, 1])

if st.button("Fetch Competitor Price"):
    competitor_price = get_competitor_price()
    st.write(f"Competitor Price: ₹{competitor_price}")
else:
    competitor_price = st.number_input("Enter Competitor Price", 50.0, 1000.0, 200.0)

if st.button("Predict Price"):
    price = dynamic_price(demand, inventory, competitor_price, season)
    st.success(f"💰 Final Price: ₹{price}")