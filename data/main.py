import json

with open("data\poi.json") as json_file:
    poi = json.load(json_file)

print(poi)
