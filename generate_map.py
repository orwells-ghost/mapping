import folium, pandas


# GPS Coords at Pioneer Courthouse
map = folium.Map(location=[39.8283, -98.5795], zoom_start=6)

# Create feature group and add to map
fg = folium.FeatureGroup(name="Pandas Map")

# Read data from csv and save to dataframe
data = pandas.read_csv("us_volcano_data.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation"])

# Loop through each list simultaneously
for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='green')))

# Add child fg (Marker) to map
map.add_child(fg)

# Save map
map.save("PandasMap.html")