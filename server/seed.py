#!/usr/bin/env python3

from app import app  # Import the Flask app
from models import db, Restaurant, Pizza, RestaurantPizza  # Import database and models

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Pizza.query.delete()  # Delete all pizzas
    Restaurant.query.delete()  # Delete all restaurants
    RestaurantPizza.query.delete()  # Delete all restaurant-pizza associations

    print("Creating restaurants...")
    restaurants = [
        Restaurant(name="Karen's Pizza Shack", address='address1'),
        Restaurant(name="Sanjay's Pizza", address='address2'),
        Restaurant(name="Kiki's Pizza", address='address3'),
        Restaurant(name="Mario's Pizzeria", address='address4'),
        Restaurant(name="Luigi's Eatery", address='address5'),
        Restaurant(name="Tony's Trattoria", address='address6'),
        Restaurant(name="Giovanni's Kitchen", address='address7'),
        Restaurant(name="Nina's Pizzeria", address='address8'),
        Restaurant(name="Bella's Pizza", address='address9'),
        Restaurant(name="Dino's Pizza", address='address10'),
        Restaurant(name="Fiona's Slice", address='address11'),
        Restaurant(name="Olivia's Oven", address='address12'),
        Restaurant(name="Pizza Palace", address='address13'),
        Restaurant(name="Rocco's Pizzeria", address='address14'),
        Restaurant(name="Vincenzo's", address='address15'),
        Restaurant(name="Alfredo's Pizza", address='address16'),
        Restaurant(name="Pepperoni Place", address='address17'),
        Restaurant(name="The Pizza Spot", address='address18'),
        Restaurant(name="Mamma Mia's", address='address19'),
        Restaurant(name="Pasta & Pizza", address='address20'),
        Restaurant(name="Zesty Pizza", address='address21'),
        Restaurant(name="Rustic Crust", address='address22'),
        Restaurant(name="Pizzeria Italia", address='address23'),
        Restaurant(name="Cheesy Bites", address='address24'),
        Restaurant(name="Artisan Pizzas", address='address25'),
        Restaurant(name="Gourmet Pizza Co.", address='address26'),
        Restaurant(name="Pizza Factory", address='address27'),
        Restaurant(name="Crust & Sauce", address='address28'),
        Restaurant(name="Slice of Heaven", address='address29'),
        Restaurant(name="Savory Slices", address='address30'),
    ]

    print("Creating pizzas...")
    pizzas = [
        Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni"),
        Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken, Red Onion, Cilantro"),
        Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Mozzarella, Ham, Pineapple"),
        Pizza(name="Meat Lover's", ingredients="Dough, Tomato Sauce, Mozzarella, Sausage, Bacon, Pepperoni"),
        Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Onions, Mushrooms"),
        Pizza(name="Buffalo Chicken", ingredients="Dough, Buffalo Sauce, Chicken, Blue Cheese"),
        Pizza(name="Four Cheese", ingredients="Dough, Tomato Sauce, Mozzarella, Cheddar, Parmesan, Goat Cheese"),
        Pizza(name="Pesto Veggie", ingredients="Dough, Pesto, Mozzarella, Spinach, Artichokes"),
        Pizza(name="Seafood Delight", ingredients="Dough, Tomato Sauce, Mozzarella, Shrimp, Clams"),
        Pizza(name="Calzone", ingredients="Dough, Ricotta, Mozzarella, Ham, Pepperoni"),
        Pizza(name="Cheeseburger", ingredients="Dough, Burger Patty, Cheese, Pickles, Onion, Ketchup"),
        Pizza(name="Greek", ingredients="Dough, Olive Oil, Feta, Olives, Tomatoes, Spinach"),
        Pizza(name="Bacon and Egg", ingredients="Dough, Mozzarella, Bacon, Egg"),
        Pizza(name="Philly Cheese Steak", ingredients="Dough, Steak, Onions, Peppers, Cheese"),
        Pizza(name="Caprese", ingredients="Dough, Tomato, Mozzarella, Basil, Balsamic Glaze"),
        Pizza(name="Mediterranean", ingredients="Dough, Tomato Sauce, Feta, Olives, Artichokes"),
        Pizza(name="Cajun Chicken", ingredients="Dough, Cajun Sauce, Chicken, Mozzarella"),
        Pizza(name="Rustic Veggie", ingredients="Dough, Tomato Sauce, Mozzarella, Seasonal Veggies"),
        Pizza(name="Truffle Mushroom", ingredients="Dough, Truffle Oil, Mushrooms, Mozzarella"),
        Pizza(name="Spicy Italian", ingredients="Dough, Tomato Sauce, Spicy Sausage, Peppers"),
        Pizza(name="Pineapple Paradise", ingredients="Dough, Tomato Sauce, Mozzarella, Pineapple, Ham"),
        Pizza(name="Roasted Garlic", ingredients="Dough, Olive Oil, Roasted Garlic, Mozzarella"),
        Pizza(name="Basil Pesto Chicken", ingredients="Dough, Basil Pesto, Chicken, Mozzarella"),
        Pizza(name="Sweet BBQ Pork", ingredients="Dough, BBQ Sauce, Pulled Pork, Onion"),
        Pizza(name="Spicy Veggie", ingredients="Dough, Spicy Tomato Sauce, Mozzarella, Hot Peppers"),
        Pizza(name="Sloppy Joe", ingredients="Dough, Sloppy Joe Mix, Cheese"),
        Pizza(name="Spinach and Feta", ingredients="Dough, Olive Oil, Spinach, Feta"),
        Pizza(name="Tandoori Chicken", ingredients="Dough, Tandoori Sauce, Chicken, Onions"),
        Pizza(name="Buffalo Cauliflower", ingredients="Dough, Buffalo Sauce, Cauliflower, Cheese"),
        Pizza(name="Taco Pizza", ingredients="Dough, Taco Sauce, Beef, Cheese, Lettuce, Tomato"),
        Pizza(name="Apple & Cheddar", ingredients="Dough, Apple, Cheddar, Cinnamon"),
        Pizza(name="S'mores Pizza", ingredients="Dough, Chocolate, Marshmallows, Graham Cracker Crust"),
        Pizza(name="Cinnamon Roll Pizza", ingredients="Dough, Cinnamon, Sugar, Icing"),
    ]

    print("Creating RestaurantPizza...")
    restaurantPizzas = []  # List to hold restaurant-pizza associations
    prices = list(range(1, 31))  # Prices from $1 to $30

    for i in range(30):
        pr = RestaurantPizza(restaurant=restaurants[i], pizza=pizzas[i], price=prices[i])  # Create association
        restaurantPizzas.append(pr)  # Add to the list

    db.session.add_all(restaurants)  # Add all restaurants to the session
    db.session.add_all(pizzas)  # Add all pizzas to the session
    db.session.add_all(restaurantPizzas)  # Add all associations to the session
    db.session.commit()  # Commit changes to the database

    print('Seeding done!')  # Indicate that seeding is complete
