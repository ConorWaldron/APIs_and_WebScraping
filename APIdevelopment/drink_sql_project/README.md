# Deployment instructions

you need to run 2 apps to get this to work, so you can do this by opening 2 terminals on your local machine
* in the first one run the backend app by using the command `python backend_app.py` this will run the backend at http://127.0.0.1:5000/ and you can see the drinks database at http://127.0.0.1:5000/drinks. You could also interact with this directly using Postman to send API requests
* in the second terminal open the front end web app with the command `python web_app.py` this will run the web app at http://127.0.0.1:5001/ and you can navigate to the different pages, you can then add drinks to the database through the website, and you can see them being added to the backend as well