import folium, pandas


# GPS Coords at Pioneer Courthouse
map = folium.Map(location=[39.8283, -98.5795], zoom_start=6)

# Create feature group and add to map
fg = folium.FeatureGroup(name="Pandas Map")

data = pandas.read_csv("us_volcano_data.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])

for lt, ln in zip(lat, lon):
	fg.add_child(folium.Marker(location=[lt, ln], popup="Hi, are you lost?", icon=folium.Icon(color='green')))

map.add_child(fg)

# Save map
map.save("PandasMap.html")