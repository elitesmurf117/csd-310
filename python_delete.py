
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.by1b1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

client = MongoClient (url)

db = client.pytech

db.module_6.find({students})

db.student.find({id:1010})

db.student.insert({id: 1010})

db.student.find({id: 1010})

db.student.remove({id: 1010})

db.student.find({students})

print = (db.list_collection_names())

print = ("end of program, press any key to exit..")
