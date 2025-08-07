# import requests

# cityName = input("Please Enter you city name: ")
# def getWeather(city):
#     api_key = "your_api_key"
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     complete_url = base_url + "q=" + city + "&appid=" + api_key
#     response = requests.get(complete_url)
#     if response.status_code == 200:
#         data = response.json()
#         main = data['main']
#         weather = data['weather'][0]
#         temperature = main['temp'] - 273.15  # Convert from Kelvin to Celsius
#         return f"City: {city}\nTemperature: {temperature:.2f}°C\nWeather: {weather['description']}"
#     else:
#         return "City not found."

# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="geoapiExercises")

# location = geolocator.geocode("Statue of Liberty, New York")

# print("Address:", location.address)
# print("Latitude:", location.latitude)
# print("Longitude:", location.longitude)


# import requests

# response = requests.get('https://ipinfo.io')
# data = response.json()
# lat, lon = data['loc'].split(',')

# print("Latitude:", lat)
# print("Longitude:", lon)

# import requests
# import os
# from dotenv import load_dotenv


# load_dotenv()
# city = input("Please Enter you city name: ")
# API_KEY = os.getenv('API_KEY')
# url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'

# response = requests.get(url).json()
# print(f"{city}: {response['current']['temp_c']}°C, {response['current']['condition']['text']}")

# streamlit_app.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Streamlit app title
st.title("Weather App 🌤️")
st.write("Enter a city name to get the current weather information.")

# Input field for city name
city = st.text_input("City Name", placeholder="Enter city name here")

# Fetch weather button
if st.button("Get Weather"):
    if city:
        # API request
        url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
        try:
            response = requests.get(url).json()
            if "error" in response:
                st.error("City not found. Please try again.")
            else:
                # Display weather information
                temp_c = response['current']['temp_c']
                condition = response['current']['condition']['text']
                icon = response['current']['condition']['icon']
                st.success(f"Weather in {city}:")
                st.image(f"http:{icon}", width=100)
                st.write(f"**Temperature:** {temp_c}°C")
                st.write(f"**Condition:** {condition}")
        except Exception as e:
            st.error("An error occurred while fetching the weather.")
    else:
        st.warning("Please enter a city name.")