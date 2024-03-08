from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from controllers import addData,fetchData
import json 

app = Flask(__name__)

with open('./config.json') as config_file:
    config_data = json.load(config_file)

@app.route('/')
def index():
    data = fetchData.getData(config_data)
    return render_template('index.html', data=data)

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        # Retrieve data from the form
        year=request.form['year']
        month = request.form['month']
        category = request.form['category']
        amount = int(request.form['amount'])
        addData.insertData(config_data,year,category,amount)
        return redirect('/')

    return render_template('add_data.html')

if __name__ == '__main__':
    app.run(debug=True)
