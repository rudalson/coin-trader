import os
import sys

project_dir = os.path.abspath(os.getcwd())
sys.path.append(project_dir)

from db.mongodb import mongodb_handler
from optparse import OptionParser
from datetime import datetime
from autotrading.machine.coinone_machine import CoinOneMachine
from autotrading.scheduler.coiner import Coiner

if __name__ == "__main__":
    machine = CoinOneMachine()
    coiner = Coiner(machine)

    result_etc = coiner.get_filled_orders(currency_pair="etc_krw")
    result_eth = coiner.get_filled_orders(currency_pair="eth_krw")
    result_btc = coiner.get_filled_orders(currency_pair="btc_krw")
    result_xrp = coiner.get_filled_orders(currency_pair="xrp_krw")

    mongodb = mongodb_handler.MongoDbHandler("local", "coiner", "price_info")
    result_list = result_etc + result_eth + result_btc + result_xrp
    ids = mongodb.insert_items(result_list)
