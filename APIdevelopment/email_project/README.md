The purpose of this project is to practice running python scripts through a REST API reuqest

# Deployment instructions

you need to run 2 apps to get this to work, so you can do this by opening 2 terminals on your local machine
* in the first one run the backend app by using the command `python email_backend_app.py` this will run the backend at http://127.0.0.1:5000/ so it will listen for API requests from either postman or the webapp
* in the second terminal open the front end web app with the command `python email_web_app.py` this will run the web app at http://127.0.0.1:5001/ and you can navigate to the different pages, run python scripts and send emails