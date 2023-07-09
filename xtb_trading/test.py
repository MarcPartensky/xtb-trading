#!/usr/bin/env python

import sys, os
import asyncio
import datetime
import logging

from XTBClient.client import XTBAsyncClient
from XTBClient.models.models import ConnectionMode, Period, Transaction, TradeOperation, TradeType
from XTBClient.models.requests import ChartLastInfoRecord, ChartRangeRecord

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

user=os.environ["USER_ID"]
password=os.environ["PASSWORD"]

async def async_client_test(user, password):
    logger = logging.getLogger("async client")

    async with XTBAsyncClient(user, password, mode=ConnectionMode.DEMO) as client:
        start = datetime.datetime.now()
        future = start.replace(year=start.year + 1)
        start = start.replace(year=start.year - 1)

        # transaction = Transaction(
        #     cmd=TradeOperation.Buy,
        #     custom_comment="Testing custom comment",
        #     expiration=future,
        #     offset=0,
        #     order=0,
        #     price=1.12,
        #     sl=0.0,
        #     symbol="EURUSD",
        #     tp=0.0,
        #     type=TradeType.Open,
        #     volume=1
        # )

        # id = await client.trade_transaction(transaction)
        # logger.info(f"Initiated transaction: {id}")

        # status = await client.transaction_status(id)
        # logger.info(f"Trade transaction status: {status}")

        # chart_info = await client.get_chart_last_request(ChartLastInfoRecord(Period.PERIOD_M5, datetime.datetime.now(), "EURPLN"))
        # logger.info(f"Last chart info: {chart_info}")

        chart_info = await client.get_chart_range_request(
            ChartRangeRecord(Period.PERIOD_M5, datetime.datetime.utcnow(), datetime.datetime.now(), "EURPLN", ticks=5))
        logger.info(f"Chart range info: {chart_info}")

        trades = await client.get_trades(False)
        logger.info(f"All trades: {trades}")

        trades = await client.get_trades_history(start=start, end=datetime.datetime.now())
        logger.info(f"All trades history: {trades}")

        await asyncio.sleep(1)

        eurpln = await client.get_symbol("EURPLN")
        logger.info(f"EURO -> PLN: {eurpln}")

        current_user = await client.get_current_user_data()
        logger.info(f"Current user: {current_user}")

        calendars = await client.get_calendar()
        logger.info(f"All calendars: {calendars}")

        await asyncio.sleep(1)

        symbols = await client.get_all_symbols()
        logger.info(f"All symbols: {symbols}")


asyncio.get_event_loop().run_until_complete(async_client_test("user", "password"))
