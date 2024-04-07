from pymongo import MongoClient
from pymongo.server_api import ServerApi
from collections import defaultdict,OrderedDict
from constants import pipelines


def formatData(monthlyData):
    formatted_data = defaultdict(list)

    for year, data in monthlyData.items():
        total_by_column = defaultdict(int)

        for month_data in data:
            income = int(month_data['Income'])
            expenses_sum = sum(month_data.get(key, 0) for key in ['Tax', 'Cash', 'Home', 'Desires', 'Travel', 'Food', 'Credit_Card'])
            
            month_data['Expenses'] = expenses_sum
            month_data['Total_Save'] = int(income - expenses_sum - month_data['Investment'])
            saving_percentage = month_data['Total_Save'] * 100 / income if income > 0 else 0
            month_data['Saving_Percentage'] = "{:.2f}".format(saving_percentage)

            for key in ['Income', 'Tax', 'Cash', 'Home', 'Desires', 'Travel', 'Food', 'Credit_Card', 'Investment', 'Expenses', 'Total_Save']:
                total_by_column[key] += int(month_data.get(key, 0))
                      
        total_data = {'month': 'Total'}
        for key, value in total_by_column.items():
            total_data[key] = value

        percent_data = {'month': '% income'}
        for key, value in total_by_column.items():
            income_percentage = (value * 100 / total_by_column['Income']) if total_by_column['Income'] != 0 else 0
            percent_data[key] = "{:.2f}".format(income_percentage)

        formatted_data[year].extend(data)
        formatted_data[year].append(total_data)
        formatted_data[year].append(percent_data)
        print(f"Year: {year} {total_data}")

    # Sort the keys before returning the result
    return dict(sorted(formatted_data.items(), key=lambda x: x[0], reverse=True))


def getData(config_data):
    # Connect to MongoDB
    mongo_data = config_data["mongo"]
    client = MongoClient(mongo_data["client"], server_api=ServerApi('1'))
    database = client[mongo_data["database"]]
    collection = database[mongo_data["collection"]]

    # Fetch data from MongoDB
    all_years = sorted(collection.distinct('year'), reverse=True)
    monthly_data_by_year = defaultdict(list)

    for year in all_years:
        # Execute aggregation pipeline
        monthly_data = list(collection.aggregate(pipelines.getQuery(year)))
        sorted_data = sorted(monthly_data, key=lambda x: x['created_at'],reverse=True)
        # print(sorted_data)
        monthly_data_by_year[year] = sorted_data
    
    data=formatData(monthly_data_by_year)
    return data
