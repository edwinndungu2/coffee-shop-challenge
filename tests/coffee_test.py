import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_init(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        
    def test_name_validation(self):
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")
        with pytest.raises(AttributeError):
            coffee = Coffee("Latte")
            coffee.name = "Mocha"
            
    def test_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        order = Order(customer, coffee, 5.0)
        assert order in coffee.orders()
        
    def test_customers(self):
        coffee = Coffee("Latte")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 6.0)
        assert len(coffee.customers()) == 2
        
    def test_num_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 6.0)
        assert coffee.num_orders() == 2
        
    def test_average_price(self):
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 7.0)
        assert coffee.average_price() == 6.0