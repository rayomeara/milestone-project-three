
A travel agent's website which is used to store bookings from customers.
The page can allow for additions, deletions and changes for bookings, flights
and hotels as needed.

---
### UX

When it came to doing this project, I had the idea of the travel agent because of
the different data they have to capture. It striked me as being one of great interest
due to the seat allocation and how a bookings app would handle it. So the application 
should handle different scenarios like the person wanted to book their holiday, 
how flights get handled when there are flight additions and cancellations, and people
who just want to make changes to bookings such as where they stay or cancel the flight.

The website opens into the bookings list. This is also the targer for the main
link on the top menu. There are also links on the top menu that point to the list
of flights and hotels.

Each of the options allows for items to be deleted or edited. Flights and hotels
can also be added and bookings are added by first indicating the destination of 
choice from the dropdown.

Wireframes from the project can be found in the 'wireframes' folder.

https://github.com/rayomeara/milestone-project-three/tree/master/wireframes

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

Also, the user stories mentioned in the UX station were all tested for. So for any
new flights added, they were checked to having been added and their seat allocation
created. The same went for flights deleted and that bookings once assigned to them
were removed. This unallocated seat was also tested to appear for any new bookings 
that are added in the future. Bookings to various destinations have all been tested.

---
### Deployment

The site is currently being hosted at:

https://rom-travel-application.herokuapp.com/

It is deployed to the site via the github repos. The application was initially
created on the heroku site named 'rom-travel-application' with the config 
variables of 'IP' (0,0,0,0), PORT (5000) and the MONGO_URI pointing to the MongoDB
for this application.

The application is linked to the heroku application using the following command:

git remote add heroku https://git.heroku.com/rom-travel-application.git

To allow the app to be deployed and recognized as a python app by heroku, a 
requirements.txt file is created using:

pip3 freeze --local > requirements.txt

The deployment will fail if this file is not created. To allow the application to 
run on Heroku, a Procfile needs to be created. This is done using:

echo web: python app.py > Procfile

Now the application can be deployed. To push the code from our app to heroku, run:

git push -u heroku master

To ensure that a web process is running by Heroku, run the following:

heroku ps:scale web=1


To run locally, clone the repository using the command:

git clone https://github.com/rayomeara/milestone-project-three.git
