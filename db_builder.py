from pymongo import MongoClient

server = MongoClient("lisa@stuy.edu")

db = server["redesigned-potato"]

Cdicts = []
lines = open("courses.csv").read().split('\n')[1:]

for line in lines:
    if line == "":
        continue;
    newdict = {}
    newdict['code'] = line.split(',')[0]
    newdict['mark'] = line.split(',')[1]
    newdict['id'] = line.split(',')[2]
    dicts.append(newdict)

db.courses.insert_many(dicts)

Pdicts = []
lines = open("courses.csv").read().split('\n')[1:]

for line in lines:
    if line == "":
        continue;
    newdict = {}
    newdict['code'] = line.split(',')[0]
    newdict['mark'] = line.split(',')[1]
    newdict['id'] = line.split(',')[2]
    dicts.append(newdict)

