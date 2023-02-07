from pymongo import MongoClient

# LOCAL DB
# db_client = MongoClient().local

# REMOTE DB
db_client =  MongoClient(
    "mongodb+srv://test1:test1@cluster0.zrplbre.mongodb.net/?retryWrites=true&w=majority").test