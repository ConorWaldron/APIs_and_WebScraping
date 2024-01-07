from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # set the URL for your database
db = SQLAlchemy(app) # create instance of database


# define your database Model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    def __repr__(self):
        return f'{self.name} - {self.description}'

# this is the home page of my website/flask web app
@app.route('/')
def index():
    return 'Hello!'


###################################### My API endpoints ########################################################

# if the database is not found, lets make one
@app.route('/create_db')
def create_db():
    with app.app_context():
        db.create_all()
        return 'Database created'

# a Get request API
@app.route('/drinks')
def get_drinks():
    all_drinks = Drink.query.all() # returns a list of Drink object instances
    # but the class drink, and the instances of that class are not JSON serialisable so we must reformat it

    # convert  list of drink instances to list of python dictionaries
    output = []
    for drink in all_drinks:
        drink_data = {'id': drink.id, 'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {'drinks': output}

# a Get request API that requires an argument
@app.route('/drink/<id>')
def get_a_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.description}

# Post method
@app.route('/drinks', methods=['POST']) # note that the url is the same as our previous get method
def add_drink():
    # we are going to add a new drink to the database, but note the function has no arugments, we get info from
    # the information from the HTTP request by using 'from flask import Flask, request'
    new_drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(new_drink)
    db.session.commit()

    # we could return Nothing, but its nice to have a success message, lets use the ID in the success message
    new_id = new_drink.id
    return f'successfully added drink to {new_id}'

# Delete method
@app.route('/drink/<id>', methods=['DELETE'])
def delete_drink(id):
    drink_to_delete = Drink.query.get(id)
    if drink_to_delete is None:
        return {'error': f'no drink found for id {id}'}
    db.session.delete(drink_to_delete)
    db.session.commit()
    # we dont need to return anything, but lets return success message
    return {'message': f'drink id {id} was deleted'}


if __name__ == '__main__':
    app.run(debug=True) # for some reason this runs on http://127.0.0.1:5000
