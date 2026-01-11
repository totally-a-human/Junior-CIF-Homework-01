weather = [
    ["monday" , [5,10, "slight rain with clouds"]] ,
    ["tuesday" , [7,11, "sunny with clouds"]] ,
    ["wednesday" , [7,12, "heavy rain with clouds"]] ,
    ["thursday" , [6,10,"light rain with clouds"]] ,
    ["friday" , [6,9, "light rain with clouds"]] ,
    ["saturday" , [4,11, "cloudy with sunny spells, light snow"]] ,
    ["sunday" , [2,11,"cloudy"]]
]
print("The weather forecast in Richmond Hill ontario from nov 3 to nov 9: ")
for day in weather:
    print(f"On {day[0]}: high = {day[1][0]}C, low = {day[1][1]}C, the weather is {day[1][2]}.")