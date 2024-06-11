import folium
import fused
import streamlit as st
from streamlit_folium import st_folium

# City coordinates map
city_coords = {
    "Paris": (48.8566, 2.3522),
    "London": (51.5074, -0.1278),
    "Sydney": (-33.8688, 151.2093),
    "Boston": (42.3601, -71.0589),
    "New York City": (40.7128, -74.0060),
    "San Francisco": (37.7749, -122.4194),
    "Twin Cities MSA": (44.9778, -93.2650),
    "Chicago": (41.8781, -87.6298),
    "Istanbul": (41.0082, 28.9784),
    "Rome": (41.9028, 12.4964),
    "Lisbon": (38.7223, -9.1393),
    "Berlin": (52.5200, 13.4050),
    "New Orleans": (29.9511, -90.0715),
    "Los Angeles": (34.0522, -118.2437),
    "Dallas": (32.7767, -96.7970),
    "Copenhagen": (55.6761, 12.5683),
    "Cape Town": (-33.9249, 18.4241),
    "Buenos Aires": (-34.6037, -58.3816),
    "Brussels": (50.8503, 4.3517),
}

# Sidebar with city selection and Resolution Selection
sidebar = st.sidebar
sidebar.markdown("# Parameter Selection")
city = sidebar.selectbox("Select City", list(city_coords.keys()))

resolution = sidebar.selectbox(
    "Select Resolution",
    [7, 8, 9, 10, 11],
)

# Get coordinates for the selected city
lat, lng = city_coords[city]

# Main Heading
st.markdown("# Airbnb Listings")

# Run UDF
TOKEN = "9f5d270f24e315148dbb2581205358d29bb599ee7455e06041caad8706457eee"
gdf = fused.run(TOKEN, city=city, resolution=int(resolution), lat=lat, lng=lng)
gdf.set_crs(epsg=4326, inplace=True)

# Generate map with dark tiles and center on selected city
m = folium.Map([lat, lng], zoom_start=10, tiles="CartoDB dark_matter")

# Generate map layers
folium.GeoJson(gdf).add_to(m)
folium.Marker(
    location=[lat, lng],
    icon=folium.Icon(icon="cloud"),
).add_to(m)

# Adjusting Map Dimensions
folium_data = st_folium(m, width=900, height=600)
print(folium_data)
