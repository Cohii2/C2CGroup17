import datetime

class Order:
    """Object representing an Order in an Order Book.

    Attributes:
        id (str): A string indicating the serial number of the order.
        quantity (int): An integer indicating the quantity of the order.
        price (float): A float indicating the price per unit of the order. 
        time (datetime.datetime): A datetime object indicating the time the order was placed. 
    """

    def __init__(self, id : str, quantity : int, price : float, time : datetime.datetime = None):
        """
        Initializes an Order object.

        Args:
            id (str): The serial number of the order.
            quantity (int): The quantity of the order.
            price (float): The price per unit of the order.
            time (datetime.datetime): The time the order was placed. If not provided, the current time will be used.
        """

        self.id = id
        self.quantity = quantity 
        self.price = price
        self.time = time if time is not None else datetime.datetime.now()
    
    def __str__(self):
        """Returns a string representation of the Order object."""
        return f"{self.__class__.__name__} | ID: {self.id} | Quantity: {self.quantity} | Price: {self.price} | Time: {self.time}"

class MarketOrder(Order):
    """Object representing a Market Order in an Order Book.

    A Market Order is an Order that does not have a specified price, and executes at market price. 

    Attributes:
        id (str): A string indicating the serial number of the order.
        quantity (int): An integer indicating the quantity of the order.
        time (datetime.datetime): A datetime object indicating the time the order was placed. 
    """

    """Default price used"""
    DEFAULT_PRICE = 0.0

    def __init__(self, id : str, quantity : int, time : datetime.datetime = None):
        """Initialises a Market Order object.
        
        Args:
            id (str): The serial number of the order.
            quantity (int): The quantity of the order.
            time (datetime.datetime): The time the order was placed. If not provided, the current time will be used.
        """
        super().__init__(id = id, quantity = quantity, price = MarketOrder.DEFAULT_PRICE, time = time)

class LimitOrder(Order):
    """Object representing a Limit Order in an Order Book.

    A Limit Order is an Order that has a specified price, and executes at specified price or better. 

    Attributes:
        id (str): A string indicating the serial number of the order.
        quantity (int): An integer indicating the quantity of the order.
        price (float): A float indicating the price per unit of the order. 
        time (datetime.datetime): A datetime object indicating the time the order was placed. 
    """

    def __init__(self, id : str, quantity : int, price : float, time : datetime.datetime = None):
        """
        Initialises a Limit Order object.
        
        Args:
            id (str): The serial number of the order.
            quantity (int): The quantity of the order.
            price (float): The price per unit of the order.
            time (datetime.datetime): The time the order was placed. If not provided, the current time will be used.
        """
        super().__init__(id = id, quantity = quantity, price = price, time = time)