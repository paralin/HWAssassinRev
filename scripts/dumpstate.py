#!/usr/bin/python

import sys
import requests
import json

if len(sys.argv) != 2:
    print "Wrong number of arguments, specify key as only argument."
    exit()

keypayload = {"key": sys.argv[1]}

r = requests.post("http://hwassassin.hwtechcouncil.com/game/get_state", data=keypayload)

if r.status_code != 200:
    print "Weird response code, "+r.status_code

data = r.json()
print json.dumps(data, indent=4, sort_keys=True)
