countries = {
    "China": 18782,
    "India": 18996,
    "USA": 33189,
    "Indonesia": 27390,
    "Pakistan": 22089,
    "Brazil": 21255
}


copyCoutries = countries.copy()

print("Top 3 most populated countries:")

for i in range(3):   
    maxCountry = None
    maxPopulation = -1
    
    for country, population in copyCoutries.items():
        if population > maxPopulation:
            maxCountry = country
            maxPopulation = population
    
print(f"{maxCountry}: {maxPopulation}")
del copyCoutries[maxCountry]
