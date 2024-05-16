from .order import MarketOrder, LimitOrder

from bisect import insort
from typing import Union
from collections import defaultdict

class OrderBook:
    """Object representing an Order Book.

    Attributes:
        bid_market_orders (List[MarketOrder]): A list of buy-side Market Orders sorted in recent order.
        bid_limit_orders (List[LimitOrder]): A list of buy-side Limit Orders sorted in descending price order.

        ask_market_orders (List[MarketOrder]): A list of sell-side Market Orders sorted in recent order. 
        ask_limit_orders (List[LimitOrder]): A list of sell-side Limit Orders sorted in ascending price order. 

        day_high_price (float): The daily high price per unit. 
        day_low_price (float): The daily low price per unit.

        transaction_history (Dict[float, int]): A Dictionary representing the transaction history, 
            with price as key and volume as value. 
    """

    def __init__(self):
        """
        Initializes an Order Book object.
        """
        self.bid_market_orders = []
        self.bid_limit_orders = []

        self.ask_market_orders = []
        self.ask_limit_orders = []

        self.day_high_price, self.day_low_price = None, None

        self.transaction_history = defaultdict(int)

    def add_bid_order(self, order : Union[MarketOrder, LimitOrder]):
        """
        Adds a buy-side order to the Order Book.

        Args:
            Order (Union[MarketOrder, LimitOrder]): The order to be added.
        """
        if isinstance(order, MarketOrder):
            insort(a = self.bid_market_orders, x = order, key = lambda order : order.time)
            return
        
        if isinstance(order, LimitOrder):
            insort(a = self.bid_limit_orders, x = order, key = lambda order : (-order.price, order.time))

    def add_ask_order(self, order : Union[MarketOrder, LimitOrder]):
        """
        Adds a sell-side order to the Order Book.

        Args:
            Order (Union[MarketOrder, LimitOrder]): The order to be added.
        """
        if isinstance(order, MarketOrder):
            insort(a = self.ask_market_orders, x = order, key = lambda order : order.time)
            return
        
        if isinstance(order, LimitOrder):
            insort(a = self.ask_limit_orders, x = order, key = lambda order : (order.price, order.time))