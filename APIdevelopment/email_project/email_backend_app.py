from flask import Flask, request

app = Flask(__name__)


# this is the home page of my website/flask web app
@app.route('/')
def index():
    return 'Hello!'


###################################### My API endpoints ########################################################

if __name__ == '__main__':
    app.run(debug=True) # for some reason this runs on http://127.0.0.1:5000
