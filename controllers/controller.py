from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def home():
    return "Gamers Stop Shop!"

@app.route('/orders')
def get_orders():
    return render_template('index.html', title="Orders", orders=orders)

@app.route('/orders/<index>')
def get_order_number(index):
    return render_template('order.html', orders=orders(int[index]))