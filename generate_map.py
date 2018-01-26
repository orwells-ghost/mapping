import folium, re, requests, bs4
from wiki_scrape import get_volDict


# GPS Coords at Pioneer Courthouse
map = folium.Map(location=[39.8283, -98.5795], zoom_start=6)

# List of coordinates
coords = [[45.518751, -122.678794], [45.520426, -122.677938],[45.521335, -122.681368], [45.518020, -122.683182], [45.517104, -122.679727]]
# Create feature group and add to map
fg = folium.FeatureGroup(name="My Map")


for coordinates in coords:
	fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

# Save map
map.save("Map1.html")