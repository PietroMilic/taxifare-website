import streamlit as st
import datetime
import requests
import streamlit as st
import datetime
import pandas as pd


'''
# Display of Our Taxifare Model
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

"""
## 1. Date and Time
"""

d = st.date_input(
    "Which date do you want to select?",
    datetime.date(2019, 7, 6))


t = st.time_input('Select the time you would like for your ride', datetime.time(8, 45))

dt = datetime.datetime.combine(d,t)

st.write('Your ride is set for', dt)

"""
## 2. Pickup and Dropoff
"""

pick_long = st.number_input('Insert the longitude of you pickup point')

st.write('The current longitude is ', pick_long)

"""
## 3. Pickup latitude
"""

pick_lat = st.number_input('Insert the latitude of you pickup point')

st.write('The current latitude is ', pick_lat)

"""
## 4. Dropoff longitude
"""

drop_long = st.number_input('Insert the longitude of you dropoff point')

st.write('The current longitude is ', drop_long)

"""
## 5. Dropoff latitude
"""

drop_lat = st.number_input('Insert the latitude of you dropoff point')

st.write('The current latitude is ', drop_lat)

"""
## 6. Passenger Count
"""

option = st.slider('Select the number of passengers', 1, 6, 1)

st.write("Number of passengers: ",option)

url = 'https://taxifare.lewagon.ai/predict'

'''
# Price for the Ride
'''
params = {
    "pickup_datetime": dt,
    "pickup_longitude": pick_long,
    "pickup_latitude": pick_lat,
    "dropoff_longitude": drop_long,
    "dropoff_latitude": drop_lat,
    "passenger_count": option
}

response = requests.get(url, params=params)

prediction = response.json()

st.write("Your estimated price is ",round(prediction["fare"],2),"$")
'''
# Your itinerary
'''
map_data = pd.DataFrame({
    "longitude":[pick_long,drop_long],
    "latitude":[pick_lat, drop_lat]
})

st.map(map_data)
