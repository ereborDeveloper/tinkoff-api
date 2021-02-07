import time
import tinvest
import math
from pprint import pprint
import KEY

TOKEN=KEY.TOKENTIN
def getBrokerId(tokenCl):
    client =tinvest.SyncClient(tokenCl, use_sandbox=True)
    return client.get_accounts().payload.accounts[0].broker_account_id

BrokerAccountId=getBrokerId(TOKEN)

def SetCurrency(tokenCl,brokerAccountId):
    client = tinvest.SyncClient(tokenCl,use_sandbox=True)
    body = tinvest.SandboxSetCurrencyBalanceRequest(
        balance=1000,
        currency='RUB',
    )
    client.set_sandbox_currencies_balance(body,brokerAccountId)

def SetPosition(tokenCl, brokerAccountId, MoneyBalans, StocksFIGI):
    client = tinvest.SyncClient(tokenCl,use_sandbox=True)
    body = tinvest.SandboxSetPositionBalanceRequest(
        balance=MoneyBalans,
        figi=StocksFIGI,
        )
    client.set_sandbox_positions_balance(body, brokerAccountId)

def getStocks(tokenCl):
    stocks = {}
    client = tinvest.SyncClient(tokenCl, use_sandbox=True)
    response = client.get_portfolio()
    positions = response.payload.positions
    for i in positions:
        key = i.name
        balance = i.balance
        stocks[key] = [float(balance), i.instrument_type.value]
    return stocks

def getStocks2(tokenCl):
    client = tinvest.SyncClient(tokenCl, use_sandbox=True)
    response = client.get_portfolio()
    positions = response.payload.positions
    print(positions)

def getMarketStocks(tokenCl):
    client =  tinvest.SyncClient(tokenCl, use_sandbox=True)
    mass=client.get_market_stocks()
    for i in mass.payload.instruments:
        print("Навазние Акции: ",i.name, "  Цена закрытия:",client.get_market_orderbook(i.figi, 5).payload.close_price," ", i.currency.value )
        time.sleep(0.02)

pprint("Hello")

# SetPosition(TOKEN, BrokerAccountId, 5, "BBG000BPL8G3")
pprint(getStocks(TOKEN))
# getMarketStocks(TOKEN)

