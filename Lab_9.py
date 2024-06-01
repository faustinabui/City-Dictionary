def city_dictionary():
    city_population = {}
    while True:
        city_name = input("Enter a city name (Enter 'done' to stop): ")
        if city_name == 'done':
            break

        city_population[city_name] = int(input(f"Enter the population of {city_name}: "))

    large_cities = {name: pop for name, pop in city_population.items() if pop > 2000000}

    return large_cities


resulting_dict = city_dictionary()


print("Cities with populations over 2 million:")
for city, population in resulting_dict.items():
    print(f"{city}: {population}")
