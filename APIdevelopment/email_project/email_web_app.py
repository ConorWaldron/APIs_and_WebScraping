from flask import Flask, request, redirect, url_for, render_template, flash
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'email_kufjhaslfihaslfhslikfhjl' #os.environ.get('not set up yet')

# Your backend API endpoint
backend_api_url = 'http://127.0.0.1:5000'

@app.route('/')
def home():
    return render_template('home.html', title="Conor's python script website")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) # for some reason this runs at  http://192.168.0.38:5000/