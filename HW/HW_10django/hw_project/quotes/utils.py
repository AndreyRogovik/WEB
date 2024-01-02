from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://localhost:10")
    db = client.hw
    return db
