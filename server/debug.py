#!/usr/bin/env python3

from app import app  # Import the Flask app
from models import db, Restaurant, Pizza, RestaurantPizza  # Import database and models

if __name__ == "__main__":
    with app.app_context():
        import ipdb; ipdb.set_trace()  # Start debugger within the app context
