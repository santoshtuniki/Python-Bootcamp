country = input('Add country name:\n')
visits = int(input('Number of visits:\n'))
list_of_cities = eval(input('List of cities visited:\n'))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, list_of_cities):
    item = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(item)


add_new_country(country, visits, list_of_cities)
print(
    f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times."
)
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
