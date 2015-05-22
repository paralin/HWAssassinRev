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

for id, plyr in edata.iteritems():
    if "player_data" in plyr:
        print id+": "+plyr["player"]["name"]+" => "+plyr["player_data"]["target_name"]
