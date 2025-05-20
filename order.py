from customer import Customer  # Make sure this import matches your project structure
from .coffee import Coffee  # Use relative import if in a package, or ensure coffee.py exists in the same directory

class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after initialization")
        self._price = price
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of type Customer")
        self._customer = customer
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        self._coffee = coffee