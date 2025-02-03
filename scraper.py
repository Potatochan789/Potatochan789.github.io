import requests
import sys
from tqdm.auto import tqdm
from bs4 import BeautifulSoup
import json
import time

urlList = [
    "https://www.smogon.com/forums/threads/scl-iv-replays.3750816/",
    "https://www.smogon.com/forums/threads/smogons-official-ladder-tournament-xi-replay-thread.3750361/",
    "https://www.smogon.com/forums/threads/smogon-premier-league-xvi-replays.3758078/"
]

def get_team_contents(url: str):
    req = requests.get(f"{url}.log", allow_redirects=True, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    })

    if req.status_code != 200:
        return None

    data = {}

    for line in req.content.decode("utf-8").split(sep="\n"):
        parsed = line.split(sep="|")
        if len(parsed) < 2:
            continue
        if parsed[1] == "player":
            tqdm.write(f"Found player {parsed[2]} with name {parsed[3]}")
            if parsed[2] in data:
                continue

            data[parsed[2]] = {
                "name": parsed[3],
                "team": [],
            }
            continue
        if parsed[1] != "poke":
            continue


        tqdm.write(f"Found pokemon {parsed[3]} owned by {parsed[2]}")
        data[parsed[2]]["team"].append(parsed[3])
        if len(data[parsed[2]]["team"]) == 6:
            data[parsed[2]]["team"].sort()


    return data

def get_all_replay_links(url: str):
    correct_links = []
    page = 1
    origUrl = url
    lastTitle = ""
    while True:
        try:
            req = requests.get(url, allow_redirects=True, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
            })


            soup = BeautifulSoup(req.content, "html.parser")
            
            title = soup.find_all("title")

            if title == lastTitle:
                return correct_links
            lastTitle = title

            links = soup.find_all("a", href=True)
            
            for link in links:
                if not ("https://replay.pokemonshowdown.com/smogtours-gen9ou" in link["href"] or "https://replay.pokemonshowdown.com/gen9ou" in link["href"]):
                    continue
                if correct_links.count(link["href"]) > 0:
                    continue
                
                correct_links.append(link["href"].split("?")[0])
            page += 1
            url = origUrl + "page-" + str(page)
            
            
        except:
            return correct_links


links = []


for url in urlList:
    links = links + get_all_replay_links(url)

for x in links:
    print(x)
tqdm.write(f"Found {len(links)} links")

output = []

for link in tqdm(links, colour="green", desc="Fetching teams.."):
    teamcontents = get_team_contents(link)

    while teamcontents == {}:
        time.sleep(0.5)
        teamcontents = get_team_contents(link)

        if teamcontents == None:
            continue

    if teamcontents == None:
        continue

    output.append({
        "link": link,
        "teams": teamcontents
    })

# print(json.dumps(output))
# print(output)

f = open("test.json", "w")
f.write(json.dumps(output))
f.close()

# testing
# print(get_team_contents("https://replay.pokemonshowdown.com/gen81v1-1907362871"))
