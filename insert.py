from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json 
from datetime import datetime, timedelta, timezone

with open('config.json') as config_file:
    config_data = json.load(config_file)

# Connect to MongoDB
mongo_data=config_data["mongo"]
client = MongoClient(mongo_data["client"],server_api=ServerApi('1'))
database = client[mongo_data["database"]]
collection = database[mongo_data["collection"]]
# Data to be inserted
data = [
    {"month": "April", "Income": [{"amount": 77467, "description": "Income for April 2022"}], "Tax": [{"amount": 0, "description": "Tax for April 2022"}], "Cash": [{"amount": 4500, "description": "Cash for April 2022"}], "Home": [{"amount": 7800, "description": "Home for April 2022"}], "Desires": [{"amount": 1800, "description": "Desires for April 2022"}], "Credit_Card": [{"amount": 32835, "description": "Credit Card for April 2022"}], "Investment": [{"amount": 21069, "description": "Investment for April 2022"}], "year": 2023, "user_id":1071},
    {"month": "May", "Income": [{"amount": 77467, "description": "Income for May 2022"}], "Tax": [{"amount": 0, "description": "Tax for May 2022"}], "Cash": [{"amount": 3000, "description": "Cash for May 2022"}], "Home": [{"amount": 2300, "description": "Home for May 2022"}], "Desires": [{"amount": 2700, "description": "Desires for May 2022"}], "Credit_Card": [{"amount": 7059, "description": "Credit Card for May 2022"}], "Investment": [{"amount": 20728, "description": "Investment for May 2022"}], "year": 2023, "user_id":1071},
    {"month": "June", "Income": [{"amount": 77467, "description": "Income for June 2022"}], "Tax": [{"amount": 0, "description": "Tax for June 2022"}], "Cash": [{"amount": 7500, "description": "Cash for June 2022"}], "Home": [{"amount": 6940, "description": "Home for June 2022"}], "Desires": [{"amount": 6700, "description": "Desires for June 2022"}], "Credit_Card": [{"amount": 10071, "description": "Credit Card for June 2022"}], "Investment": [{"amount": 21133, "description": "Investment for June 2022"}], "year": 2023, "user_id":1071},
    {"month": "July", "Income": [{"amount": 77467, "description": "Income for July 2022"}], "Tax": [{"amount": 0, "description": "Tax for July 2022"}], "Cash": [{"amount": 1500, "description": "Cash for July 2022"}], "Home": [{"amount": 1700, "description": "Home for July 2022"}], "Desires": [{"amount": 12000, "description": "Desires for July 2022"}], "Credit_Card": [{"amount": 47067, "description": "Credit Card for July 2022"}], "Investment": [{"amount": 20994, "description": "Investment for July 2022"}], "year": 2023, "user_id":1071},
    {"month": "August", "Income": [{"amount": 66857, "description": "Income for August 2022"}], "Tax": [{"amount": 0, "description": "Tax for August 2022"}], "Cash": [{"amount": 9500, "description": "Cash for August 2022"}], "Home": [{"amount": 3935, "description": "Home for August 2022"}], "Desires": [{"amount": 2300, "description": "Desires for August 2022"}], "Credit_Card": [{"amount": 38904, "description": "Credit Card for August 2022"}], "Investment": [{"amount": 20722, "description": "Investment for August 2022"}], "year": 2023, "user_id":1071},
    {"month": "September", "Income": [{"amount": 0, "description": "Income for September 2022"}], "Tax": [{"amount": 0, "description": "Tax for September 2022"}], "Cash": [{"amount": 7000, "description": "Cash for September 2022"}], "Home": [{"amount": 13000, "description": "Home for September 2022"}], "Desires": [{"amount": 3000, "description": "Desires for September 2022"}], "Credit_Card": [{"amount": 29226, "description": "Credit Card for September 2022"}], "Investment": [{"amount": 21103, "description": "Investment for September 2022"}], "year": 2023, "user_id":1071},
    {"month": "October", "Income": [{"amount": 90634, "description": "Income for October 2022"}], "Tax": [{"amount": 12018, "description": "Tax for October 2022"}], "Cash": [{"amount": 12000, "description": "Cash for October 2022"}], "Home": [{"amount": 81645, "description": "Home for October 2022"}], "Desires": [{"amount": 10780, "description": "Desires for October 2022"}], "Credit_Card": [{"amount": 9785, "description": "Credit Card for October 2022"}], "Investment": [{"amount": 24268, "description": "Investment for October 2022"}], "year": 2023, "user_id":1071},
    {"month": "November", "Income": [{"amount": 146200, "description": "Income for November 2022"}], "Tax": [{"amount": 0, "description": "Tax for November 2022"}], "Cash": [{"amount": 1000, "description": "Cash for November 2022"}], "Home": [{"amount": 9976, "description": "Home for November 2022"}], "Desires": [{"amount": 6637, "description": "Desires for November 2022"}], "Credit_Card": [{"amount": 21460, "description": "Credit Card for November 2022"}], "Investment": [{"amount": 24739, "description": "Investment for November 2022"}], "year": 2023, "user_id":1071},
    {"month": "December", "Income": [{"amount": 146180, "description": "Income for December 2022"}], "Tax": [{"amount": 0, "description": "Tax for December 2022"}], "Cash": [{"amount": 800, "description": "Cash for December 2022"}], "Home": [{"amount": 5522, "description": "Home for December 2022"}], "Desires": [{"amount": 16927, "description": "Desires for December 2022"}], "Credit_Card": [{"amount": 48283, "description": "Credit Card for December 2022"}], "Investment": [{"amount": 24571, "description": "Investment for December 2022"}], "year": 2023, "user_id":1071},
    {"month": "January", "Income": [{"amount": 140332, "description": "Income for January 2023"}], "Tax": [{"amount": 5868, "description": "Tax for January 2023"}], "Cash": [{"amount": 18600, "description": "Cash for January 2023"}], "Home": [{"amount": 10110, "description": "Home for January 2023"}], "Desires": [{"amount": 10835, "description": "Desires for January 2023"}], "Credit_Card": [{"amount": 23805, "description": "Credit Card for January 2023"}], "Investment": [{"amount": 24562, "description": "Investment for January 2023"}], "year": 2023, "user_id":1071},
    {"month": "February", "Income": [{"amount": 140332, "description": "Income for February 2023"}], "Tax": [{"amount": 5868, "description": "Tax for February 2023"}], "Cash": [{"amount": 800, "description": "Cash for February 2023"}], "Home": [{"amount": 9834, "description": "Home for February 2023"}], "Desires": [{"amount": 10819, "description": "Desires for February 2023"}], "Credit_Card": [{"amount": 13345, "description": "Credit Card for February 2023"}], "Investment": [{"amount": 19614, "description": "Investment for February 2023"}], "year": 2023, "user_id":1071},
    {"month": "March", "Income": [{"amount": 140333, "description": "Income for March 2023"}], "Tax": [{"amount": 93028, "description": "Tax for March 2023"}], "Cash": [{"amount": 500, "description": "Cash for March 2023"}], "Home": [{"amount": 10420, "description": "Home for March 2023"}], "Desires": [{"amount": 34961, "description": "Desires for March 2023"}], "Credit_Card": [{"amount": 54177, "description": "Credit Card for March 2023"}], "Investment": [{"amount": 19653, "description": "Investment for March 2023"}], "year": 2023, "user_id":1071}
]


# Adding the "year" field to each document
count=1
for entry in data:
    count+=1
    entry["created_at"]= datetime.now()-timedelta(hours=count)

# Insert data into MongoDB collection using insert_many
collection.insert_many(data)
# result = collection.delete_many({})
# Close MongoDB connection
client.close()
