import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_init(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
        
    def test_name_validation(self):
        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")
            
    def test_orders(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order in customer.orders()
        
    def test_coffees(self):
        customer = Customer("Alice")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        Order(customer, coffee1, 5.0)
        Order(customer, coffee2, 4.5)
        assert len(customer.coffees()) == 2