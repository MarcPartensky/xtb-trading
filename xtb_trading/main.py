#!/usr/bin/env python

import os
from dotenv import load_dotenv
from XTBApi.api import Client

load_dotenv()

USER_ID = os.environ["USER_ID"]
PASSWORD = os.environ["PASSWORD"]

client = Client()

def check_if_market_open():

# CHECK IF MARKET IS OPEN FOR EURUSD
    # client.login(USER_ID, PASSWORD, mode="demo")
    client.login(USER_ID, PASSWORD)
    client.check_if_market_open("EURUSD")

# # BUY ONE VOLUME (FOR EURUSD THAT CORRESPONDS TO 100000 units)
# # client.open_trade('buy', EURUSD, 1)
# # SEE IF ACTUAL GAIN IS ABOVE 100 THEN CLOSE THE TRADE
# trades = client.update_trades() # GET CURRENT TRADES
# trade_ids = [trade_id for trade_id in trades.keys()]
# for trade in trade_ids:
#     actual_profit = client.get_trade_profit(trade) # CHECK PROFIT
#     if actual_profit >= 100:
#         client.close_trade(trade) # CLOSE TRADE
# # CLOSE ALL OPEN TRADES
# client.close_all_trades()

    client.logout()
