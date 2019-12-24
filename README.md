
A travel agent's website which is used to store bookings from customers.
The page can allow for additions, deletions and changes for bookings, flights
and hotels as needed.

---
### UX

The website opens into the bookings list. This is also the targer for the main
link on the top menu. There are also links on the top menu that point to the list
of flights and hotels.

Each of the options allows for items to be deleted or edited. Flights and hotels
can also be added and bookings are added by first indicating the destination of 
choice from the dropdown.

---
### Technologies

HTML5,
CSS3,
Javascript,
Bootstrap 3.4.1,
JQuery 3.4.1,
Python 3,
Flask
MongoDB

---
### Features/Design

The application uses a HTML/CSS/Javascript front end to display information
coming from a Python controller class which is connected to a Mongo database.
The python controller is using Flask as a means of handling web requests
from the front end and PyMongo as the interface between Python and MongoDB.

As described in previous chapters, this app allows for the edit/add/delete of
the booking/flight/hotel objects. As part of the flight object, seats are also
maintained based on the number of seats indicated for each flight. So, for 
initial creation, seats are created and any adjustment of that figure in edits
causes seats to be added or deleted. Flight deletion handles the deletion of
those seats.

Also, the booking creation is done by using the country of destination as an
initial parameter. This was done for the reason that this parameter is used
to drive data like the appropriate flights for that destination and the 
appropriate hotels. 

The seat dropdown is driven by the flight selected, so this is done by 
making an independent non-submit request to the python controller via 
Javascript and the data is returned using jsonify which the javasript 
handles and re-populates the seat dropdown with the available seats for that
flight. It should also be noted that any new bookings or seat changes will
cause a booking_no flag to be added/deleted for any seats selected/de-selected.

---
### Features to do

One feature that would be a nice to have would be a nicer graphical interface
to allow the person to see where the seat is on the flight when it is selected.
It was left out because because this is a project more focused on the data, it's
not an absolute necessity.

Another feature that would an addition is a better means of handling flights or
hotels which are deleted but are still assigned with some booking. In this case,
preventing the booking from being deleted would be an option or returning a 
warning to the user that because this data is being removed, a potential number
of bookings need to be adjusted and assigned a new flight/hotel.

---
### Testing

All testing done was manual. This involved checking that the basic CRUD operations
on bookings/hotels/flights worked. Also some basic UI testing to make sure all of
the links work in the menu bar. Testing was done to ensure that any changes or
deletions to objects were handled correctly and that the user was able to edit a 
booking to allow for a new flight/hotel to be selected.

Testing was done for the seat handling in case of changes which would cause a 
seat to be allocated/deallocated from/to a particular booking. This was confirmed
by checking that a new booking has access to seats deallocated by a booking 
and that seats now allocated were not selectable from the dropdown. This was also
thoroughly checked for changing flights which caused the jsonify update to trigger
on the seats dropdown.

---
### Deployment

The site is currently being hosted at:

https://rom-travel-application.herokuapp.com/

It is deployed to the site via the github repos. To deploy to the website, run:

get remote add heroku https://git.heroku.com/rom-travel-application.git
git push heroku master

To run locally, clone the repository using the command:

git clone https://github.com/rayomeara/milestone-project-three.git