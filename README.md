#  Project Name
PIZZA RESTAURANT API

## Overview
The Pizza Restaurant API is a Flask-based web application that allows users to manage and retrieve information about restaurants and the pizzas they offer. This project provides a RESTful API for tracking restaurants, their menu items, and the prices of each pizza.

## Project Structure
server/app.py: The main Flask application file containing route definitions and API logic.
server/models.py: Defines the data models for Restaurant, Pizza, and RestaurantPizza, including their relationships and validations.
server/seed.py: Script to populate the database with initial data for testing.
server/test_import.py: A simple script to test the import of the Flask application.

## Features
Retrieve a list of all restaurants
Get detailed information about a specific restaurant
Retrieve a list of all pizzas
Create new associations between restaurants and pizzas with pricing
Data validation for pizza prices

## Installation

### Setup
Ensure you have Python and pipenv installed on your system.
Clone the repository and navigate to the project directory.
Set up the virtual environment and install dependencies:
   
   pipenv install
   pipenv shell
   
    Set up the database:
   
   export FLASK_APP=server/app.py
   flask db init
   flask db upgrade head
   python server/seed.py
   

## Running the Application
Start the Flask backend:

python server/app.py


## API Endpoints
GET /restaurants: Retrieve a list of all restaurants
GET /restaurants/:id: Get detailed information about a specific restaurant
GET /pizzas: Retrieve a list of all pizzas
POST /restaurant_pizzas: Create a new association between a restaurant and a pizza

## Data Models
Restaurant: Represents a restaurant with attributes like name and address.
Pizza: Represents a pizza with attributes such as name and ingredients.
RestaurantPizza: Represents the association between a restaurant and a pizza, including the price of the pizza at that restaurant.


## Future Enhancements
Implement user authentication and authorization
Add more complex querying capabilities (e.g., finding pizzas by ingredient)
Incorporate a review system for pizzas and restaurants
Develop a frontend interface for easier interaction with the API


## Contributing
Contributions to the PIZZA RESTAURANT API project are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.









