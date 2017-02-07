##Rodda John y Jiaqi Gao
##SoftDev2 pd8
##HW2 -- You Boys Like Mexico?
##2017-02-06  

from pymongo import MongoClient

#server = MongoClient('localhost', 27017)
server = MongoClient("lisa.stuy.edu")

db = server["redesigned-potato"]

db.courses.remove()
db.peeps.remove()

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
for person in db.peeps.find():
    nombre = person["name"]
    eyedee = person["id"]
    avg = 0
    num = 0
    for course in db.courses.find({'id': eyedee}):
        avg += int(course["mark"])
        num += 1

    avg = float(avg) / float(num)
    print("Name: "+nombre+" ID: "+eyedee+" Avg: "+str(avg))

                   


