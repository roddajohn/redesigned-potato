##Rodda John y Jiaqi Gao
##SoftDev2 pd8
##HW3 -- Welcome to Tijuana
##2017-02-08

from pymongo import MongoClient

server = MongoClient("lisa.stuy.edu")

db = server["redesigned-potato"]

db.teachers.remove()

t_dicts = []

# insert teachers
for line in open('teachers.csv').read().split('\n'):
    if line == '':
        continue

    new_dict = {}
    new_dict['course_name'] = line.split(',')[0]
    new_dict['teacher'] = line.split(',')[1]
    new_dict['period'] = line.split(',')[2]

    list_of_students = []
    #find student ides who take this class w/ this teacher
    for course in db.courses.find({'code': new_dict['course_name']}):
        list_of_students.append(course['id'])

    new_dict['students'] = list_of_students

    t_dicts.append(new_dict)

db.teachers.insert_many(t_dicts)
        

# query stuff
for person in db.peeps.find():
    nombre = person["name"]
    eyedee = person["id"]
    avg = 0
    num = 0
    #calculate average
    for course in db.courses.find({'id': eyedee}):
        avg += int(course["mark"])
        num += 1

    avg = float(avg) / float(num)

    # print schtuff
    print("Name: "+nombre+" ID: "+eyedee+" Avg: "+str(avg))
