import os
import requests
import json
from time import sleep
from bs4 import BeautifulSoup

def get_team_information(team_name):

    r = requests.get(f"https://www.premierinjuries.com/teams/{team_name}")
    soup = BeautifulSoup(r.content, "html.parser")

    rows = soup.find_all("tr", class_="player-row")

    player_results = []

    for row in rows:

        element = row.find_all("td")
        name = element[0].text.replace("Player", "")
        reason = element[1].text.replace("Reason", "")
        details = element[2].text.replace("Further Detail", "")
        potential_return = element[3].text.replace("Potential Return", "")
        condition = element[4].text.replace("Condition", "")
        status = element[5].text.replace("Status", "")

        player_results.append({
            "name": name,
            "reason": reason,
            "details": details,
            "potential_return": potential_return,
            "condition": condition,
            "status": status
        })

    return player_results


team_names = [
        "afc-bournemouth",
        "arsenal",
        "aston-villa",
        "brentford",
        "brighton-hove-albion",
        "chelsea",
        "crystal-palace",
        "everton",
        "fulham",
        "leeds-united",
        "leicester-city",
        "liverpool",
        "manchester-city",
        "manchester-united",
        "newcastle-united",
        "nottingham-forest",
        "southampton",
        "tottenham-hotspur",
        "west-ham-united",
        "wolverhampton-wanderers"
]

team_data = []

for team_name in team_names:
    print(f"Fetching {team_name} information...")
    team_data.append({
        "team_name": team_name,
        "players": get_team_information(team_name)
    })
    print("Sleeping for 10...")
    sleep(10)

script_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(script_path, "webpage", "src", "team_data.json"), "w") as f:
    json.dump(team_data, f)
