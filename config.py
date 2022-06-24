import pymongo

Mongo_Database = "mongodb://localhost:27017"

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["FastAPI"]
student_collection = database["student"]




