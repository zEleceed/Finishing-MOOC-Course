def sort_by_seasons(items: list):
    def seasons(dictionary: dict):
        return dictionary["seasons"]

    return sorted(items, key=seasons)


shows = [{"name": "Dexter", "rating": 8.6, "seasons": 9}, {"name": "Friends", "rating": 8.9, "seasons": 10},
         {"name": "Simpsons", "rating": 8.7, "seasons": 32}]

for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")
