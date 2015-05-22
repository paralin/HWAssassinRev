#!/usr/bin/python

import sys
import requests
import shlex
import json

args = shlex.split(" ".join(sys.argv[1:]))
edata = {}

if len(args) != 1:
    print "Wrong number of arguments, specify dump as only argument."
    exit()

with open(args[0], "r") as myfile:
    edata = json.loads(myfile.read().strip())

img = ""
with open("profile.base64", "r") as myfile:
    img = myfile.read().strip()

# Get all players from top_players
players = {}

i = 0
for plyr in edata["top_players"]:
    i+=1
    print str(i)+"/"+str(len(edata["top_players"]))+" Fetching "+plyr["name"]
    reg = {
        "name": plyr["name"],
        "year": plyr["year"],
        "school_id": plyr["school_id"],
        "image": img
    }

    r = requests.post("http://hwassassin.hwtechcouncil.com/players/add_player", data=reg)

    if r.status_code != 200:
        print "Weird response code for "+plyr["name"]+", "+r.status_code
    else:
        data = r.json()
        nplyr = {"key": data["key"]}

        print " => key = "+nplyr["key"]

        r = requests.post("http://hwassassin.hwtechcouncil.com/game/get_state", data=nplyr)

        data = r.json()
        nplyr["player"] = data["player"]
        if "player_data" in data:
            nplyr["player_data"] = data["player_data"]
        players[plyr["school_id"]] = nplyr

print json.dumps(players)
