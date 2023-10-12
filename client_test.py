import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
           'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
           'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            average = (bid_price + ask_price) / 2
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(bid_price, quote['top_bid']['price'])
            self.assertEqual(ask_price, quote['top_ask']['price'])
            self.assertEqual(price, average)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
                  {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
                  {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
            ]
        stocks = []
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            try:
                self.assertGreater(bid_price, ask_price)
                stocks.append(stock)
            except AssertionError:
                pass
        print(stocks)

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_calculateBid_or_AskPriceZeroReturnsNone(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            result = getDataPoint(quote)
            self.assertIsNone(result)

    def test_getRatio_PriceBzero_ReturnNone(self):

        prices = {'ABC': 120.84, 'DEF': 0}
        result = getRatio(prices['ABC'], prices['DEF'])
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
