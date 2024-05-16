from dataclasses import dataclass, field
import datetime

@dataclass
class Order:
    """Object representing an Order in an Order Book.

    Attributes:
        id (str): A string indicating the serial number of the order.
        quantity (int): An integer indicating the quantity of the order.
        price (float): A float indicating the price per unit of the order. 
        time (datetime.datetime): A datetime object indicating the time the order was placed. 
    """
    id : str
    quantity : int 
    price : float 
    time : datetime.datetime = field(default_factory = datetime.datetime.now)
    
    def __str__(self):
        """Returns a string representation of the Order object."""
        return f"{self.__class__.__name__} | ID: {self.id} | Quantity: {self.quantity} | Price: {self.price} | Time: {self.time}"

@dataclass
class MarketOrder(Order):
    """Object representing a Market Order in an Order Book.

    A Market Order is an Order that does not have a specified price, and executes at market price. 

    Attributes:
        id (str): A string indicating the serial number of the order.
        quantity (int): An integer indicating the quantity of the order.
        time (datetime.datetime): A datetime object indicating the time the order was placed. 
    """
    price : float = field(default = 0.0)

@dataclass
class LimitOrder(Order):
    """Object representing a Limit Order in an Order Book.

    A Limit Order is an Order that has a specified price, and executes at specified price or better. 

    Attributes:
        id (str): A string indicating the serial number of the order.
        quantity (int): An integer indicating the quantity of the order.
        price (float): A float indicating the price per unit of the order. 
        time (datetime.datetime): A datetime object indicating the time the order was placed. 
    """