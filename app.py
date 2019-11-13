import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = 'mongodb+srv://root:pass@myfirstcluster-2scdt.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bookings')
def get_bookings():
    return render_template("bookings.html")


@app.route('/get_flights')
def get_flights():
    return render_template("flights.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
