#!/usr/bin/python

import sys
import requests
import shlex
import json

args = shlex.split(" ".join(sys.argv[1:]))

img = ""
with open("profile.base64", "r") as myfile:
    img = myfile.read().strip()

if len(args) != 3:
    print "Wrong number of arguments, specify name, year, school id"
    exit()

reg = {
    "name": args[0],
    "year": args[1],
    "school_id": args[2],
    "image": img
}

r = requests.post("http://hwassassin.hwtechcouncil.com/players/add_player", data=reg)

if r.status_code != 200:
    print "Weird response code, "+r.status_code

data = r.json()
print json.dumps(data, indent=4, sort_keys=True)
