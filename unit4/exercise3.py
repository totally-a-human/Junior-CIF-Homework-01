def miles_to_km(miles):
    km = miles * 1.6
    print (f"{miles} miles is equal to {km} kilometers.")
    return km   

results = miles_to_km(float(input("Enter distance in miles: ")))
print (results)