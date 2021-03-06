from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init db
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)

#Product Class - Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), unique = True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  quantity = db.Column(db.Integer)
  
  def __init__(self, name, description, price, quantity):
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity
    
#Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'quantity')
    
#Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)  

#Create a product
@app.route('/product', methods = ['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  quantity = request.json['quantity']
  
  new_product = Product(name,description,price,quantity)
  
  db.session.add(new_product)
  db.session.commit()
  
#return single product  
  return product_schema.jsonify(new_product)


#Running development server
if __name__ == '__main__':
  app.run(debug=True)