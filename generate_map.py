import folium, pandas

# Read data from csv and save to dataframe
data = pandas.read_csv("volcano_locations_world.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
data.Elevation*=3.28084 # Convert meters to feet
elev = list(data["Elevation"])
vName = list(data["Volcano Name"])

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

# # Loop through each list simultaneously
# for lt, ln, el, vn in zip(lat, lon, elev, vName):
# 	string = vn + ": " + str(el) + " feet"
# 	fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(string), fill_color=color_producer(el), 
# 		color='grey', fill_opacity=0.7, radius=2500))

# Load json file with world geo data
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'), 
	style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
	else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Add child fg (Marker) to
map.add_child(fg)

# Save map
map.save("PandasMap.html")