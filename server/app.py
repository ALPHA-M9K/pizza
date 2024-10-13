from flask import Flask, make_response, jsonify, request  # Import necessary modules from Flask
from flask_migrate import Migrate  # Import migration tools
from flask_restful import Api, Resource  # Import API and Resource for RESTful structure
from models import db, Restaurant, RestaurantPizza, Pizza  # Import database and models
import os  # Import os module for environment variable handling

# Set the base directory and database URI
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")  # Use DB_URI from environment or default to SQLite

app = Flask(__name__)  # Initialize Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE  # Set the database URI for SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
app.json.compact = False  # Set JSON output format

db.init_app(app)  # Initialize the database with the Flask app
migrate = Migrate(app, db)  # Set up migration support
api = Api(app)  # Create an API instance

@app.route('/')  # Define the root route
def index():
    return '<h1>Code challenge</h1>'  # Return a simple message

# Resource for handling restaurant-related API calls
class Restaurants(Resource):
    def get(self):
        # Retrieve all restaurants and convert them to a dictionary format
        restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        return make_response(jsonify(restaurants), 200)  # Return restaurants as JSON

# Resource for handling individual restaurant API calls
class RestaurantByID(Resource):
    def get(self, id):
        # Retrieve a specific restaurant by ID
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            return make_response(jsonify(restaurant.to_dict()), 200)  # Return the restaurant data
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)  # Handle not found error

    def delete(self, id):
        # Delete a specific restaurant by ID
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            db.session.delete(restaurant)  # Remove the restaurant from the session
            db.session.commit()  # Commit changes to the database
            return make_response('', 204)  # Return no content response
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)  # Handle not found error

# Resource for handling pizza-related API calls
class Pizzas(Resource):
    def get(self):
        # Retrieve all pizzas and convert them to a dictionary format
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
        return make_response(jsonify(pizzas), 200)  # Return pizzas as JSON

# Resource for creating associations between restaurants and pizzas
class RestaurantPizzas(Resource):
    def post(self):
        # Create a new association between a restaurant and a pizza
        data = request.get_json()  # Get the JSON data from the request
        
        try:
            new_restaurant_pizza = RestaurantPizza(
                price=data['price'],  # Set price from request data
                pizza_id=data['pizza_id'],  # Set pizza ID from request data
                restaurant_id=data['restaurant_id']  # Set restaurant ID from request data
            )
            db.session.add(new_restaurant_pizza)  # Add the new association to the session
            db.session.commit()  # Commit changes to the database
            return make_response(jsonify(new_restaurant_pizza.pizza.to_dict()), 201)  # Return the created pizza data
        except ValueError as e:
            return make_response(jsonify({"errors": [str(e)]}), 400)  # Handle validation errors

# Add resources to the API with their respective endpoints
api.add_resource(Restaurants, '/restaurants')
api.add_resource(RestaurantByID, '/restaurants/<int:id>')
api.add_resource(Pizzas, '/pizzas')
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

if __name__ == "__main__":
    app.run(port=5555, debug=True)  # Run the app in debug mode on port 5555
