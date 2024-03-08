from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json 
from collections import defaultdict



def insertData(config_data,year,month,category,amount):
    # Connect to MongoDB
    mongo_data=config_data["mongo"]
    client = MongoClient(mongo_data["client"],server_api=ServerApi('1'))
    database = client[mongo_data["database"]]
    collection = database[mongo_data["collection"]]


    # Insert data into MongoDB
    collection.insert_one({
            "year":year,
            "month": month,
            f"{category}": amount,
        })   