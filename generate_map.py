import folium, pandas

# Read data from csv and save to dataframe
data = pandas.read_csv("us_volcano_data.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation"])

def color_producer(elev):
	"""
	Returns color depending on elevation group
	Input: elevation int
	Output: Color
	"""
	if elev < -1000:
		return 'darkred'
	elif -1000 <= elev < 0:
		return 'red'
	elif 0 <= elev < 1000:
		return 'lightblue'
	elif 1000 <= elev < 2000:
		return 'blue'
	elif elev >= 2000:
		return 'darkblue'
	else:
		return 'black'

# GPS Coords at Pioneer Courthouse
map = folium.Map(location=[39.8283, -98.5795], zoom_start=6)

# Create feature group and add to map
fg = folium.FeatureGroup(name="Pandas Map")

# Loop through each list simultaneously
for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color=color_producer(el))))

# Add child fg (Marker) to
map.add_child(fg)

# Save map
map.save("PandasMap.html")