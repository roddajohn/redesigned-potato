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
    Cdicts.append(newdict)

db.courses.insert_many(Cdicts)

Pdicts = []
lines = open("peeps.csv").read().split('\n')[1:]

for line in lines:
    if line == "":
        continue;
    newdict = {}
    newdict['name'] = line.split(',')[0]
    newdict['age'] = line.split(',')[1]
    newdict['id'] = line.split(',')[2]
    Pdicts.append(newdict)

db.courses.insert_many(Pdicts)

