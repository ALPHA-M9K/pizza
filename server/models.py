#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for ORM
from sqlalchemy import MetaData  # Import MetaData for naming conventions
from sqlalchemy.orm import validates  # Import validates for field validation
from sqlalchemy.ext.associationproxy import association_proxy  # Import for association proxy
from sqlalchemy_serializer import SerializerMixin  # Import for serialization

# Set up naming conventions for foreign keys
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)  # Initialize SQLAlchemy with the defined metadata

# Model representing a restaurant
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'  # Define table name

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String)  # Restaurant name
    address = db.Column(db.String)  # Restaurant address

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')
    pizzas = association_proxy('restaurant_pizzas', 'pizza')  # Proxy to access pizzas directly

    serialize_rules = ('-restaurant_pizzas.restaurant', '-pizzas.restaurants')  # Define serialization rules

    def __repr__(self):
        return f'<Restaurant {self.name}>'  # String representation of the restaurant

# Model representing a pizza
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'  # Define table name

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String)  # Pizza name
    ingredients = db.Column(db.String)  # Pizza ingredients

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')  # Link to RestaurantPizza
    restaurants = association_proxy('restaurant_pizzas', 'restaurant')  # Proxy to access restaurants directly

    serialize_rules = ('-restaurant_pizzas.pizza', '-restaurants.pizzas')  # Define serialization rules

    def __repr__(self):
        return f'<Pizza {self.name}, {self.ingredients}>'  # String representation of the pizza

# Model representing the association between restaurants and pizzas
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'  # Define table name

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    price = db.Column(db.Integer, nullable=False)  # Price of the pizza at this restaurant
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))  # Foreign key to restaurants
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))  # Foreign key to pizzas

    # Relationships
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')  # Link to Restaurant
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')  # Link to Pizza

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas')  # Define serialization rules

    @validates('price')  # Validate price field
    def validate_price(self, key, price):
        if not 1 <= price <= 30:  # Ensure price is between 1 and 30
            raise ValueError("Price must be between 1 and 30")
        return price  # Return valid price

    def __repr__(self):
        return f"<RestaurantPizza ${self.price}>" # String representation of the restaurant-pizza association
