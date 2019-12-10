import env # COMMENT THIS OUT WHEN DEPLOYING TO HEROKU
import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "booking_db"
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'ENV Value Not Loaded')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bookings')
def get_bookings():
    return render_template("bookings.html", bookings=mongo.db.booking.find(), countries=mongo.db.country.find())


@app.route("/add_booking", methods=['POST'])
def add_booking():
    country = request.form.get('destination')
    flights = mongo.db.flight.find({'country_to': country})
    seats = mongo.db.seat.find({'flight_no': flights[0]["flight_no"], 'booking_no': {'$exists': False}})
    return render_template('addbooking.html',
                            country=country,
                            flights=flights,
                            seats=seats,
                            hotels=mongo.db.hotel.find({'country': country}))


@app.route("/insert_booking", methods=['POST'])
def insert_booking():
    flight_no = request.form.get("flight_no")
    seat_no = request.form.get("seat_no")
    booking_no = request.form.get("booking_no")
    seat = mongo.db.seat
    seat.update({'seat_no': seat_no, 'flight_no': flight_no}, {
            'booking_no': booking_no,
            'seat_no': seat_no,
            'flight_no': flight_no
    })
    booking = mongo.db.booking
    booking.insert_one(request.form.to_dict())
    return redirect(url_for('get_bookings'))


@app.route('/edit_booking/<booking_id>')
def edit_booking(booking_id):
    prev_booking = mongo.db.booking.find_one({'_id': ObjectId(booking_id)})
    flights = mongo.db.flight.find({'country_to': prev_booking["country_to"]})
    seats = mongo.db.seat.find({'flight_no': flights[0]["flight_no"], '$or': [{'booking_no': {'$exists': False}}, {'booking_no': prev_booking['booking_no']}]})
    hotels = mongo.db.hotel.find({'country': prev_booking["country_to"]})
    return render_template('editbooking.html', booking=prev_booking, flights=flights, seats=seats, hotels=hotels)


@app.route('/update_booking/<booking_id>', methods=["POST"])
def update_booking(booking_id):
    flight_no = request.form.get("flight_no")
    seat_no = request.form.get("seat_no")
    booking_no = request.form.get("booking_no")
    seat = mongo.db.seat
    seat.update({'booking_no': booking_no}, {
            '$unset': {"booking_no": ""}
    })
    seat.update({'seat_no': seat_no, 'flight_no': flight_no}, {
            'booking_no': booking_no,
            'seat_no': seat_no,
            'flight_no': flight_no
    })
    bookings = mongo.db.booking
    bookings.update({'_id': ObjectId(booking_id)},
        {
            'booking_no': request.form.get('booking_no'),
            'full_name': request.form.get('full_name'),
            'flight_no': request.form.get('flight_no'),
            'country_to': request.form.get('country_to'),
            'hotel_name': request.form.get('hotel_name'),
            'extra_baggage': request.form.get('extra_baggage'),
            'first_class': request.form.get('first_class'),
            'seat_no': request.form.get('seat_no')
        })
    return redirect(url_for('get_bookings'))


@app.route('/delete_booking/<booking_id>')
def delete_booking(booking_id):
    mongo.db.booking.delete_one({'_id': ObjectId(booking_id)})
    return redirect(url_for('get_bookings'))


@app.route('/get_flights')
def get_flights():
    return render_template("flights.html", flights=mongo.db.flight.find())


@app.route("/add_flight")
def add_flight():
    return render_template('addflight.html',
                            countries=mongo.db.country.find())


@app.route("/insert_flight", methods=['POST'])
def insert_flight():
    flight = mongo.db.flight
    flight.insert_one(request.form.to_dict())
    return redirect(url_for('get_flights'))


@app.route('/edit_flight/<flight_id>')
def edit_flight(flight_id):
    prev_flight = mongo.db.flight.find_one({'_id': ObjectId(flight_id)})
    countries = mongo.db.country.find()
    return render_template('editflight.html', flight=prev_flight, countries=countries)


@app.route('/update_flight/<flight_id>', methods=["POST"])
def update_flight(flight_id):
    flight = mongo.db.flight
    flight.update({'_id': ObjectId(flight_id)},
        {
            'flight_no': request.form.get('flight_no'),
            'country_to': request.form.get('country_to'),
            'seats': request.form.get('seats')
        })
    return redirect(url_for('get_flights'))


@app.route('/delete_flight/<flight_id>')
def delete_flight(flight_id):
    mongo.db.flight.delete_one({'_id': ObjectId(flight_id)})
    return redirect(url_for('get_flights'))


@app.route('/get_hotels')
def get_hotels():
    return render_template("hotels.html", hotels=mongo.db.hotel.find())


@app.route("/add_hotel")
def add_hotel():
    return render_template('addhotel.html',
                            countries=mongo.db.country.find())


@app.route("/insert_hotel", methods=['POST'])
def insert_hotel():
    hotel = mongo.db.hotel
    hotel.insert_one(request.form.to_dict())
    return redirect(url_for('get_hotels'))


@app.route('/edit_hotel/<hotel_id>')
def edit_hotel(hotel_id):
    prev_hotel = mongo.db.hotel.find_one({'_id': ObjectId(hotel_id)})
    countries = mongo.db.country.find()
    return render_template('edithotel.html', hotel=prev_hotel, countries=countries)


@app.route('/update_hotel/<hotel_id>', methods=["POST"])
def update_hotel(hotel_id):
    hotel = mongo.db.hotel
    hotel.update({'_id': ObjectId(hotel_id)},
        {
            'hotel_id': request.form.get('hotel_id'),
            'hotel_name': request.form.get('hotel_name'),
            'country': request.form.get('country'),
            'rating': request.form.get('rating')
        })
    return redirect(url_for('get_hotels'))


@app.route('/delete_hotel/<hotel_id>')
def delete_hotel(hotel_id):
    mongo.db.hotel.delete_one({'_id': ObjectId(hotel_id)})
    return redirect(url_for('get_hotels'))


@app.route("/get_seats")
def get_seats():
    flight = request.args.get('flight')
    booking = request.args.get('booking')
    if flight:
        seats = mongo.db.seat.find({'flight_no': flight, '$or': [{'booking_no': {'$exists': False}}, {'booking_no': booking}]})
        data = [{'seat_id': seat[0]} for seat in seats]
    return jsonify(data)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
