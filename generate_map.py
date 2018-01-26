import folium
from wiki_scrape import get_volDict


# GPS Coords at Pioneer Courthouse
map = folium.Map(location=[39.8283, -98.5795], zoom_start=6)

# Create feature group and add to map
fg = folium.FeatureGroup(name="My Map")

# Get dictionary of volcanoes from scripe
volDict = get_volDict()

for volcano in volDict:
	fg.add_child(folium.Marker(location=volDict[volcano][1], popup=("%s - Elevation: %s") % (volcano, volDict[volcano][0]), icon=folium.Icon(color='green')))

map.add_child(fg)

# Save map
map.save("Map1.html")