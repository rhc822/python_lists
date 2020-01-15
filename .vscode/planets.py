planet_list = ["Mercury", "Mars"]
last_two_planets = ["Uranus", "Neptune"]
print("Initiallist: ", planet_list,"\n")

planet_list.append("Jupiter")
planet_list.append("Saturn")
print("After appending: ", planet_list,"\n")
planet_list.extend(last_two_planets)
print("After extending: ", planet_list,"\n")
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print("After inserting: ", planet_list,"\n")
planet_list.append("Pluto")
print("After appending Pluto: ", planet_list,"\n")
rocky_planets = slice(0, 4)
print("Rocky planets: ", planet_list[rocky_planets],"\n")
del planet_list[8]
print("Minus poor Pluto: ", planet_list,"\n")