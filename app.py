import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "booking_db"
app.config["MONGO_URI"] = 'mongodb+srv://root:pass@myfirstcluster-2scdt.mongodb.net/booking_db?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bookings')
def get_bookings():
    return render_template("bookings.html", bookings=mongo.db.booking.find(), countries=mongo.db.country.find())


@app.route("/add_booking", methods=['POST'])
def add_booking():
    country = request.form.get('destination')
    return render_template('addbooking.html',
                            country=country,
                            flights=mongo.db.flight.find({'country_to': country}),
                            hotels=mongo.db.hotel.find({'country': country}))


@app.route("/insert_booking", methods=['POST'])
def insert_booking():
    booking = mongo.db.booking
    booking.insert_one(request.form.to_dict())
    return redirect(url_for('get_bookings'))


@app.route('/edit_booking/<booking_id>')
def edit_booking(booking_id):
    prev_booking = mongo.db.booking.find_one({'_id': ObjectId(booking_id)})
    print(prev_booking)
    flights = mongo.db.flight.find({'country_to': prev_booking.country_to})
    hotels = mongo.db.hotel.find({'country': prev_booking.country_to})
    return render_template('editbooking.html', booking=prev_booking, flights=flights, hotels=hotels)


@app.route('/update_booking/<booking_id>', methods=["POST"])
def update_booking(booking_id):
    bookings = mongo.db.booking
    bookings.update({'_id': ObjectId(booking_id)},
        {
            'full_name': request.form.get('full_name'),
            'flight_no': request.form.get('flight_no'),
            'hotel_name': request.form.get('hotel_name'),
            'extra_baggage': request.form.get('extra_baggage'),
            'first_class': request.form.get('first_class'),
        })
    return redirect(url_for('get_bookings'))


@app.route('/delete_booking/<booking_id>')
def delete_booking(booking_id):
    mongo.db.booking.delete_one({'_id': ObjectId(booking_id)})
    return redirect(url_for('get_bookings'))


@app.route('/get_flights')
def get_flights():
    return render_template("flights.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
