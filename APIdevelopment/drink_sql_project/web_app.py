from flask import Flask, request, redirect, url_for, render_template, flash
import os
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nglahfolaihfjlaidhgfouidahflkjsnh' #os.environ.get('DRINKS_WEB_APP')


# Your backend API endpoint
backend_api_url = 'http://127.0.0.1:5000'

# this is the home page of my website/flask web app
@app.route('/')
def home():
    return render_template('home.html', title="Conor's drinks website")

@app.route('/view_drinks')
def view_drinks():
    # Make a GET request to the backend API to retrieve all drinks
    response = requests.get(backend_api_url+'/drinks')

    if response.status_code == 200:
        # Extract the drinks data from the API response
        drinks_data = response.json()['drinks']

        return render_template('view_drinks.html', drinks=drinks_data, title="Conor's drinks database")
    else:
        # Display an error message or handle the error accordingly
        return f'Something went wrong, maybe you need to run the /create_db route?' \
               f'Error: {response.status_code} - {response.text}'


@app.route('/add_drink', methods=['GET', 'POST'])
def add_drink():
    if request.method == 'POST':
        # Get the data from the form
        drink_name = request.form['drink_name']
        description = request.form['description']

        # Prepare the data for the API request
        api_data = {
            "name": drink_name,
            "description": description
        }

        # Make a POST request to the backend API
        response = requests.post(backend_api_url+'/drinks', json=api_data)

        # Check response to see if it worked
        if response.status_code == 200:
            # take the success message from the back end api and display it to the user
            message = response.text
            flash(message, 'success')
        else:
            message = f'Error: {response.status_code} - {response.text}'
            flash(message, 'danger')
        return redirect(url_for('home'))


    # If it's a GET request, display the form
    return render_template('add_drink.html', title='Add a New Drink')


@app.route('/delete_drink', methods=['GET', 'POST'])
def delete_drink():
    if request.method == 'POST':
        # Get the selected drink ID from the form
        drink_id = request.form['drink_id']
        print(f'Received POST request with form data: {request.form}')

        # Make a DELETE request to the backend API endpoint /drink/{id}
        response = requests.delete(f'{backend_api_url}/drink/{drink_id}')

        if response.status_code == 200:
            # Handle the success response
            message = response.text
            flash(message, 'success')
        else:
            # Handle errors
            flash(f'Error when trying to delete drink id {drink_id}: {response.status_code} - {response.text}', 'danger')
        return redirect(url_for('home'))

    else:
        # Make a GET request to the backend API to retrieve all drinks
        response = requests.get(f'{backend_api_url}/drinks')

        if response.status_code == 200:
            # Extract the drinks data from the API response
            drinks_data = response.json()['drinks']

            return render_template('delete_drink.html', drinks=drinks_data, title='Delete a Drink')
        else:
            # Handle errors
            return f'Error: {response.status_code} - {response.text}'


@app.route('/create_db')
def create_db():
    # Make a GET request to the backend API endpoint /create_db
    response = requests.get(f'{backend_api_url}/create_db')

    if response.status_code == 200:
        # Handle the success response
        flash('database_create_success', 'success')
    else:
        # Handle errors
        flash(f'Error: {response.status_code} - {response.text}', 'danger')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) # for some reason this runs at  http://192.168.0.38:5000/