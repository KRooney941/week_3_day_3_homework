from app import app
from flask import render_template
from models.order_list import orders


@app.route('/')
def index():
    return "OHHHH orders!"

# in brackets will look for index.html folder


@app.route('/orders')
def get_orders():
    return render_template('index.html', title="Home Page", orders=orders)


@app.route('/single_orders')
def get_single_order():
    return render_template('orders.html', title="Individual Orders", orders=orders)
