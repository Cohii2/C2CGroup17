import datetime, unittest

from matching_engine.order import MarketOrder, LimitOrder
from matching_engine.order_book import OrderBook

class TestOrderBook(unittest.TestCase):
    """Unit tests for the OrderBook class."""

    bid_orders = [
        MarketOrder(id = '001', quantity = 1, time = datetime.time(hour = 8, minute = 0, second = 0)),
        MarketOrder(id = '002', quantity = 2, time = datetime.time(hour = 8, minute = 0, second = 0)),
        MarketOrder(id = '003', quantity = 3, time = datetime.time(hour = 9, minute = 30, second = 0)),
        MarketOrder(id = '004', quantity = 4, time = datetime.time(hour = 7, minute = 30, second = 0)),

        LimitOrder(id = '005', quantity = 5, price = 5.0, time = datetime.time(hour = 8, minute = 0, second = 0)),
        LimitOrder(id = '006', quantity = 6, price = 10.0, time = datetime.time(hour = 8, minute = 0, second = 0)),
        LimitOrder(id = '007', quantity = 7, price = 15.0, time = datetime.time(hour = 8, minute = 0, second = 0)),
        LimitOrder(id = '008', quantity = 8, price = 5.0, time = datetime.time(hour = 7, minute = 30, second = 0)),
        LimitOrder(id = '009', quantity = 9, price = 10.0, time = datetime.time(hour = 9, minute = 30, second = 0)),
        LimitOrder(id = '010', quantity = 10, price = 15.0, time = datetime.time(hour = 7, minute = 30, second = 0))
    ]

    def setUp(self):
        self.order_book = OrderBook()

        for order in self.bid_orders:
            self.order_book.add_bid_order(order)
            self.order_book.add_ask_order(order)

    def tearDown(self):
        pass

    def test_bid_order_sort(self):
        """Tests that Bid Orders are sorted in specified order"""
        assert [order.id for order in self.order_book.bid_market_orders] == ['004', '001', '002', '003']
        assert [order.id for order in self.order_book.bid_limit_orders] == ['010', '007', '006', '009', '008', '005']

    def test_ask_order_sort(self):
        """Tests that Ask Orders are sorted in specified order"""
        assert [order.id for order in self.order_book.ask_market_orders] == ['004', '001', '002', '003']
        assert [order.id for order in self.order_book.ask_limit_orders] == ['008', '005', '006', '009', '010', '007']

if __name__ == '__main__':
    unittest.main()