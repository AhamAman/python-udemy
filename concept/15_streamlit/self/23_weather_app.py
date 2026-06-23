import streamlit as st
import requests

st.set_page_config(page_title="Climate Analytics Terminal", page_icon="🌤️", layout="centered")

# Operational Token Config Boundary
OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

# Cache calls to the same city for 15 minutes to save API quotas
@st.cache_data(ttl=900, show_spinner="Interrogating weather telemetry grids...")
def fetch_city_climate_vector(city_string, api_key):
    """Dispatches a parameterized GET request containing authorization credentials."""
    if api_key == "YOUR_OPENWEATHER_API_KEY":
        # Safe fallback mock data if user hasn't supplied a key yet
        return {
            "status": "MOCK_PREVIEW",
            "name": city_string.capitalize(),
            "main": {"temp": 22.5, "humidity": 65, "pressure": 1012},
            "weather": [{"description": "scattered clouds processing cleanly", "icon": "03d"}],
            "wind": {"speed": 4.1}
        }
        
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_string,
        "appid": api_key,
        "units": "metric" # Output standard Celsius format scale
    }
    
    response = requests.get(url, params=params, timeout=5.0)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        st.error("Authentication Error: Your API Secret key configuration sequence is invalid.")
        return None
    else:
        st.warning(f"Location Vector Unmapped: '{city_string}' not found in registry.")
        return None

# =====================================================================
# USER PORT CANVAS
# =====================================================================
st.title("Climate Telemetry Engine Terminal 🌤️")
st.write("Queries global meteorological REST frameworks via authenticated parameter gateways.")

st.write("---")

# User input text vector trigger
target_city = st.text_input("Enter target city name location:", value="London").strip()

if target_city:
    weather_payload = fetch_city_climate_vector(target_city, OPENWEATHER_API_KEY)
    
    if weather_payload:
        if "status" in weather_payload and weather_payload["status"] == "MOCK_PREVIEW":
            st.caption("⚠️ Running inside Offline Sandbox Mock View. Update the `OPENWEATHER_API_KEY` token string variable to enable real live endpoints.")
            
        st.write("---")
        st.header(f"Meteorological Report: {weather_payload['name']}")
        
        # Unpack nested JSON tracking variables
        temp_value = weather_payload['main']['temp']
        humidity_value = weather_payload['main']['humidity']
        wind_speed = weather_payload['wind']['speed']
        conditions = weather_payload['weather'][0]['description']
        
        # Display structural readout cards
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Ambient Temperature", value=f"{temp_value}°C")
        c2.metric(label="Relative Air Humidity", value=f"{humidity_value}%")
        c3.metric(label="Wind Vector Speed", value=f"{wind_speed} m/s")
        
        st.write("---")
        st.info(f"**Current Structural Conditions Layer:** {conditions.capitalize()}")