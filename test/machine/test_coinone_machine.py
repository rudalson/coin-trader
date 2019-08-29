import os
import unittest
from autotrading.machine.coinone_machine import CoinOneMachine
import inspect


class CoinOneMachineTestCase(unittest.TestCase):
    def setUp(self):
        project_dir = os.path.abspath(os.getcwd())
        print(os.path.abspath(project_dir))
        self.coinone_machine = CoinOneMachine()

    def tearDown(self):
        pass

    def test_set_token(self):
        print(inspect.stack()[0][3])
        expire, access_token, refresh_token = self.coinone_machine.set_token("old")
        assert access_token
        print(access_token)

    def test_get_wallet_status(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.get_wallet_status()
        assert result
        print(result)

    def test_get_ticker(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.get_ticker(currency_type="btc")
        assert result
        print(result)

    def test_buy_order(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.buy_order(currency_type="btc",
                                                price="12_300_000",
                                                qty="0.001",
                                                order_type="limit")
        assert result
        print(result)

    def test_sell_order(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.sell_order(currency_type="btc",
                                                 price="12_900_000",
                                                 qty="0.001",
                                                 order_type="limit")
        assert result
        print(result)

    def test_cancel_order(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.cancel_order(currency_type="btc",
                                                   price="12_900_000",
                                                   qty="0.001",
                                                   order_type="sell",
                                                   order_id="2efbc834-1e4d-11e9-9ec7-00e04c3600d7")
        assert result
        print(result)

    def test_get_list_my_orders(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.get_list_my_orders(currency_type="btc")
        assert result
        print(result)

    def test_get_my_order_status(self):
        print(inspect.stack()[0][3])
        result = self.coinone_machine.get_my_order_status(currency_type="btc",
                                                          order_id="2efbc834-1e4d-11e9-9ec7-00e04c3600d7")
        assert result
        print(result)


if __name__ == '__main__':
    unittest.main()
