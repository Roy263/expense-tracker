from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json 
from collections import defaultdict



def getData(config_data):
    # Connect to MongoDB
    mongo_data=config_data["mongo"]
    client = MongoClient(mongo_data["client"],server_api=ServerApi('1'))
    database = client[mongo_data["database"]]
    collection = database[mongo_data["collection"]]

    # Fetch data from MongoDB
    all_years = sorted(collection.distinct('year'), reverse=True)
    monthly_data_by_year = defaultdict(list)
    for year in all_years:
        # Query MongoDB for monthly data for the specific year
        monthly_data = list(collection.find({'year': year}))
        monthly_data_by_year[year] = monthly_data
    for year, data in monthly_data_by_year.items():
        total_by_column = defaultdict(int)
        for month_data in data:
            income = int(month_data['Income'])
            # Calculate the sum of expenses for each month
            expenses_sum = sum([month_data['Tax'], month_data['Cash'], month_data['Home'], month_data['Desires'], month_data['Credit_Card']])
            month_data['Expenses']=expenses_sum
            month_data['Total_Save']=int(income-expenses_sum-month_data['Investment'])
            saving_percentage = month_data['Total_Save'] * 100 / income if income > 0 else 0
            month_data['Saving_Percentage'] = "{:.2f}".format(saving_percentage)

            for key in ['Income', 'Tax', 'Cash', 'Home', 'Desires', 'Credit_Card', 'Investment','Expenses','Total_Save']:
                total_by_column[key] += int(month_data.get(key, 0))

        total_data = {'month': 'Total'}
        for key, value in total_by_column.items():
            total_data[key] = value
        percent_data = {'month': '% income'}
        for key, value in total_by_column.items():
            income_percentage = value *100/total_by_column['Income']
            percent_data[key] =  "{:.2f}".format(income_percentage)

        data.append(total_data)
        data.append(percent_data)
        print(f"Year: {year} {total_data}")
    return monthly_data_by_year
