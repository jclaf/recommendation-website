import logging as lg
#from .views import app

# Create database connection object
from .extensions import db


# Define models

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float, nullable=True, default=0.0)
    review_count = db.Column(db.Integer, nullable=True, default=0)

    def __init__(self, name, description, price, stock, category, image_url=None,rating=0.0, review_count=0):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.image_url = image_url
        self.rating = rating
        self.review_count = review_count

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

# Create tables in the database
#db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    lg.warning('Database initialized!')