import os
import sys

from db.mongodb import mongodb_handler
from autotrading.machine.coinone_machine import CoinOneMachine
from autotrading.scheduler.coiner import Coiner

project_dir = os.path.abspath(os.getcwd())
sys.path.append(project_dir)

if __name__ == "__main__":
    machine = CoinOneMachine()
    coiner = Coiner(machine)

    # result_etc = coiner.get_filled_orders(currency_pair="etc_krw")
    result_eth = coiner.get_filled_orders(currency_pair="eth")
    result_btc = coiner.get_filled_orders(currency_pair="btc")
    # result_xrp = coiner.get_filled_orders(currency_pair="xrp")

    mongodb = mongodb_handler.MongoDbHandler("local", "coiner", "price_info")
    result_list = result_eth + result_btc
    ids = mongodb.insert_items(result_list)
