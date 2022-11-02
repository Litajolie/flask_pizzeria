from flask import render_template
from models.order_list import order_list
from app import app


@app.route('/orders')
def order():
    return render_template('order.html', orders=order_list)

@app.route('/orders/<index>')
def detail(index):
    return render_template('order_details.html', order=order_list[int(index) - 1], index=index)