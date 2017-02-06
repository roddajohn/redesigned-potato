##Rodda John y Jiaqi Gao
##SoftDev2 pd8
##HW2 -- You Boys Like Mexico?
##2017-02-06  

from pymongo import MongoClient

#server = MongoClient("lisa@stuy.edu")
server = MongoClient()
server = MongoClient('localhost', 27017)

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

db.peeps.insert_many(Pdicts)

averages = {}
for person in db.peeps.find():
    nombre = person["name"]
    eyedee = person["id"]
    #print eyedee
    markers = db.courses.find({'id': eyedee})

    for mark in markers:
        averages[nombre] = mark
#print averages

