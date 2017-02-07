##Rodda John y Jiaqi Gao
##SoftDev2 pd8
##HW2 -- You Boys Like Mexico?
##2017-02-06  

from pymongo import MongoClient

#server = MongoClient('localhost', 27017)
server = MongoClient("lisa.stuy.edu")

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

#Calculates the avgs of all students and puts it in a dictionary where name : avg
averages = {}
for person in db.peeps.find():
    nombre = person["name"]
    eyedee = person["id"]
    markers = db.courses.find_one({'id': eyedee})
    courses = markers["courses"]
    avg = 0
    for c in courses:
        avg += int(course["mark"])
    print("Name: "+nombre+" ID: "+eyedee+" Avg: "+avg)

                   


