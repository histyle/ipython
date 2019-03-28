import pymongo


client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
dbName = client["runoobdb"]


dbList = client.list_database_names()

if "runoobdb" in dbList:
    print("The database already exists")

else:
    print("The database does not exist")


collection = dbName["sites"]

collectionList = dbName.list_collection_names()

if "sites" in collectionList:
    print("the collection already exists")
else:
    print("the collection does not exits")


#insert
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
#collection.insert_one(mydict)
x = collection.insert_one(mydict)
 
print(x.inserted_id)

