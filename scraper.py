import requests
import sys
from tqdm.auto import tqdm
from bs4 import BeautifulSoup
import json
import time

urlList = [
    "https://www.smogon.com/forums/threads/cappl-x-usage-stats-and-replays-full-stats-18.3745481/",
    "https://www.smogon.com/forums/threads/capcl-iv-usage-stats-replays.3759396/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-round-1.3760064/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonal-round-2.3760519/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonal-round-3-losers-only.3760930/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-round-4.3761285/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonal-round-5-losers-only.3761674/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonal-round-6.3762041/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-round-7-losers-only.3762432/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonal-round-8.3762801/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-round-9-losers-only.3763173/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-round-10.3763517/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-round-11-losers-finals.3763931/",
    "https://www.smogon.com/forums/threads/2025-cap-winter-seasonals-grand-finals-won-by-lbn.3764235/",
    "https://www.smogon.com/forums/threads/cappl-xi-replays.3766192/"
]

def get_team_contents(url: str):
    headers = {"User-Agent": "PostmanRuntime/7.32.3"}
    driver = {"headers": [headers]}
    req = requests.get(f"{url}.log", headers=headers)

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
            headers = {"User-Agent": "PostmanRuntime/7.32.3"}
            driver = {"headers": [headers]}
            req = requests.get(f"{url}.log", headers=headers)

            print(req)

            soup = BeautifulSoup(req.content, "html.parser")
            
            title = soup.find_all("title")

            if title == lastTitle:
                return correct_links
            lastTitle = title

            links = soup.find_all("a", href=True)
            
            for link in links:
                if not ("https://replay.pokemonshowdown.com/smogtours-gen9cap" in link["href"] or "https://replay.pokemonshowdown.com/gen9cap" in link["href"]):
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

if len(links) > 0:
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
