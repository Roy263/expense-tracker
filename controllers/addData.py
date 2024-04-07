from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime
from collections import defaultdict

def insertData(config_data, year, month, category, amount, desc):
    # Connect to MongoDB
    mongo_data = config_data["mongo"]
    client = MongoClient(mongo_data["client"], server_api=ServerApi('1'))
    database = client[mongo_data["database"]]
    collection = database[mongo_data["collection"]]

    # Get the current datetime
    current_datetime = datetime.datetime.now()

    # Check if the document exists for the given year and month
    existing_document = collection.find_one({"year": year, "month": month})

    if existing_document:
        # Update the existing document by appending to the existing category or creating a new category
        update_data = {
            f"{category}": {"amount": amount, "description": desc}
        }
        collection.update_one({"_id": existing_document["_id"]}, {"$push": update_data})
    else:
        # Create a new document with the given year, month, and category data
        new_document = {
            "year": year,
            "month": month,
            f"{category}": [{"amount": amount, "description": desc}],
            "created_at": current_datetime
        }
        collection.insert_one(new_document)
