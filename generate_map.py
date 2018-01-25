import folium

# GPS Coords at Pioneer Courthouse
map = folium.Map(location=[45.518751, -122.678794], zoom_start=15)

# Create feature group and add to map
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[45.518751, -122.678794], popup="Hi I am a marker", icon=folium.Icon(color='green')))
map.add_child(fg)

# Save map
map.save("Map1.html")