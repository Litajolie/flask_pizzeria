class Order:

    def __init__(self, customer_name, order_date, quantity, name):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.pizza_toppings = []
        self.pizza_name = name

    def add_toppings(self, *args):
        toppings = []
        for topping in args:
            toppings.append(topping)
        self.pizza_toppings = toppings
