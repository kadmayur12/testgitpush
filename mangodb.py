import pymongo
client = pymongo.MongoClient("mongodb+srv://Mayur:839017@cluster0.retuvxy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "sudhanshu" ,
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
collections = db1['test']