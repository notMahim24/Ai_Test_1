import streamlit as st
import requests

st.title("🏠 California House Price Predictor")

# Sidebar for inputs
st.sidebar.header("House Details")
med_inc = st.sidebar.slider("Median Income ($10k units)", 0.5, 15.0, 3.5)
house_age = st.sidebar.slider("House Age", 1, 52, 20)
ave_rooms = st.sidebar.slider("Average Rooms", 1, 10, 5)
ave_bed = st.sidebar.slider("Average Bedrooms", 1, 5, 1)
pop = st.sidebar.number_input("Population", value=1000)
occup = st.sidebar.slider("Average Occupancy", 1, 6, 3)
lat = st.sidebar.number_input("Latitude", value=34.05)
lon = st.sidebar.number_input("Longitude", value=-118.24)

# Deployment URL (Change this once Render gives you a link!)
BACKEND_URL = "http://localhost:8000/predict" 

if st.button("Get Estimated Price"):
    payload = {
        "MedInc": med_inc, "HouseAge": house_age, "AveRooms": ave_rooms,
        "AveBedrms": ave_bed, "Population": pop, "AveOccup": occup,
        "Latitude": lat, "Longitude": lon
    }
    
    try:
        response = requests.post(BACKEND_URL, json=payload)
        result = response.json()
        price = result["estimated_price_usd"]
        st.success(f"### Estimated Value: ${price:,.2f}")
    except Exception as e:
        st.error(f"Could not connect to Backend. Error: {e}")