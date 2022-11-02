from models.order import *
import datetime

order_1 = Order("Patrick", datetime.datetime.now().strftime("%c"), 2, "Pepperoni")
order_1.add_toppings("pepperoni", "tomato sauce")

order_2 = Order("Sandy", datetime.datetime.now().strftime("%c"), 2, "Hawaiian")
order_2.add_toppings("pineapple", "ham", "tomato sauce")

order_list = [order_1, order_2]