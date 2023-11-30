import json


def read_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def all_team_names(what):
    pass

def all_countries(country):
    pass


def execute():
    filename = input("file name: ")
    player_Data = read_data(filename)
    print(f'read the data of {len(player_Data)} players')

    print("commands:\n"
          "0 quit\n"
          "1 search for player\n"
          "2 teams\n"
          "3 countries\n"
          "4 players in team\n"
          "5 players from country\n"
          "6 most points\n"
          "7 most goals")






execute()