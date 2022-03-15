import folium

map = folium.Map(location = [0.5715890566941896, 37.6920867552808],zoom_start = 6.3 , tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name= "My Map")

fg.add_child(folium.Marker(location= [-0.15445458925218736, 37.26146953760587], popup = "Mt. Climbing" , icon = folium.Icon(color= 'beige')))
fg.add_child(folium.Marker(location= [0.5880604055069205, 36.38354743552203], popup = "Magical Game conservancy" , icon = folium.Icon(color= 'beige')))

map.add_child(fg)

map.save("Map1.html")