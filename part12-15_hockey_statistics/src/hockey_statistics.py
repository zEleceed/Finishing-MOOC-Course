import json


def formatted_string(player: dict):
    final_string = (f"{player['name']: <21}{player['team']} {player['goals']:>3} +"
                    f"{player['assists']:>3} = {player['goals'] + player['assists']:>3}")
    return final_string


def read_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def search_for_player(data, player_name):
    found = None
    for i in data:
        if i['name'] == player_name:
            found = i
            break  # Break the loop if the player is found
    if found is not None:
        return formatted_string(found)
    else:
        return "Player not found"


def all_team_names(teams):
    return sorted(set([data["team"] for data in teams]))


def all_countries(country):
    return sorted(set(nationality["nationality"] for nationality in country))


def list_players_by_points(data, team):
    found = []
    for player in data:
        if player['team'] == team:
            found.append(player)
    return sorted(found, key=lambda player_total: player_total["goals"] + player_total['assists'], reverse=True)


def list_players_by_country(data, country):
    found = [person_in_country for person_in_country in data if person_in_country['nationality'] == country]
    return sorted(found, key=lambda player_total: player_total["goals"] + player_total['assists'], reverse=True)


def most_points(data, player_range):
    def player_total_score(player: dict):
        return (player["goals"] + player["assists"]), player["goals"]

    found = sorted(data, key=lambda x: player_total_score(x), reverse=True)
    return found[:player_range]


def most_goals(data, player_range):
    def total_goals(player: dict):
        return player['goals'], (player['games'])*(-1)

    player_list = sorted(data, key=lambda x: total_goals(x), reverse=True)

    return player_list[:player_range]


def execute():
    filename = input("file name: ")
    player_Data = read_data(filename)
    print(f'read the data of {len(player_Data)} players')
    print()
    print("commands:\n"
          "0 quit\n"
          "1 search for player\n"
          "2 teams\n"
          "3 countries\n"
          "4 players in team\n"
          "5 players from country\n"
          "6 most points\n"
          "7 most goals")
    print()

    while True:
        try:
            command_input = int(input("command: "))
        except ValueError:
            print('Invalid input. Please enter an integer.')
            continue

        if command_input == 0:
            break
        elif command_input == 1:
            player_name = input("name: ")
            print(search_for_player(player_Data, player_name))
        elif command_input == 2:
            for i in all_team_names(player_Data):
                print(i)
        elif command_input == 3:
            for i in all_countries(player_Data):
                print(i)
        elif command_input == 4:
            team = input('team: ')
            needed_list = list_players_by_points(player_Data, team)
            for name in needed_list:
                print(formatted_string(name))
        elif command_input == 5:
            country = input("country: ")
            country_players = list_players_by_country(player_Data, country)
            for name in country_players:
                print(formatted_string(name))
        elif command_input == 6:
            player_range = int(input("how many: "))
            for i in most_points(player_Data, player_range):
                print(formatted_string(i))
            pass
        elif command_input == 7:
            player_range = int(input("how many: "))
            for i in most_goals(player_Data, player_range):
                print(formatted_string(i))
            pass


execute()
