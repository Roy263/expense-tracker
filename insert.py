from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json 

with open('config.json') as config_file:
    config_data = json.load(config_file)

# Connect to MongoDB
mongo_data=config_data["mongo"]
client = MongoClient(mongo_data["client"],server_api=ServerApi('1'))
database = client[mongo_data["database"]]
collection = database[mongo_data["collection"]]
# Data to be inserted
data = [
    {"month": "April", "Income": 77467, "Tax": 0, "Cash": 4500, "Home": 7800, "Desires": 1800, "Credit_Card": 32835, "Investment": 21069},
    {"month": "May", "Income": 77467, "Tax": 0, "Cash": 3000, "Home": 2300, "Desires": 2700, "Credit_Card": 7059, "Investment": 20728},
    {"month": "June", "Income": 77467, "Tax": 0, "Cash": 7500, "Home": 6940, "Desires": 6700, "Credit_Card": 10071, "Investment": 21133},
    {"month": "July", "Income": 77467, "Tax": 0, "Cash": 1500, "Home": 1700, "Desires": 12000, "Credit_Card": 47067, "Investment": 20994},
    {"month": "August", "Income": 66857, "Tax": 0, "Cash": 9500, "Home": 3935, "Desires": 2300, "Credit_Card": 38904, "Investment": 20722},
    {"month": "September", "Income": 0, "Tax": 0, "Cash": 7000, "Home": 13000, "Desires": 3000, "Credit_Card": 29226, "Investment": 21103},
    {"month": "October", "Income": 90634, "Tax": 12018, "Cash": 12000, "Home": 81645, "Desires": 10780, "Credit_Card": 9785, "Investment": 24268},
    {"month": "November", "Income": 146200, "Tax": 0, "Cash": 1000, "Home": 9976, "Desires": 6637, "Credit_Card": 21460, "Investment": 24739},
    {"month": "December", "Income": 146180, "Tax": 0, "Cash": 800, "Home": 5522, "Desires": 16927, "Credit_Card": 48283, "Investment": 24571},
    {"month": "January", "Income": 140332, "Tax": 5868, "Cash": 18600, "Home": 10110, "Desires": 10835, "Credit_Card": 23805, "Investment": 24562},
    {"month": "February", "Income": 140332, "Tax": 5868, "Cash": 800, "Home": 9834, "Desires": 10819, "Credit_Card": 13345, "Investment": 19614},
    {"month": "March", "Income": 140333, "Tax": 93028, "Cash": 500, "Home": 10420, "Desires": 34961, "Credit_Card": 54177, "Investment": 19653}
]


# Adding the "year" field to each document
for entry in data:
    entry["year"] = 2023

# Insert data into MongoDB collection using insert_many
collection.insert_many(data)

# Close MongoDB connection
client.close()
