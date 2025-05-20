import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_init(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
        
    def test_price_validation(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(TypeError):
            Order(customer, coffee, "5")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)
        order = Order(customer, coffee, 5.0)
        with pytest.raises(AttributeError):
            order.price = 6.0
            
    def test_relationships(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order in Order.all
        assert order in customer.orders()
        assert order in coffee.orders()