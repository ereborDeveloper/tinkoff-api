import tinvest
import KEY

TOKEN=KEY.TOKENTIN

print(type(TOKEN))
def SetCurrency(tokenCl,brokerAccountId):
    client = tinvest.SyncClient(tokenCl,use_sandbox=True)
    body = tinvest.SandboxSetCurrencyBalanceRequest(
        balance=1000,
        currency='RUB',
    )
    client.set_sandbox_currencies_balance(body,brokerAccountId)




def SetPosition(tokenCl, brokerAccountId):
    client = tinvest.SyncClient(tokenCl,use_sandbox=True)
    body = tinvest.SandboxSetPositionBalanceRequest(
        balance=1000,
        figi='BBG0013HGFT4',
        )
    client.set_sandbox_positions_balance(body, brokerAccountId)




def getStocks(tokenCl):
    stocks = {}
    client = tinvest.SyncClient(tokenCl, use_sandbox=True)
    response = client.get_portfolio()
    positions = response.payload.positions

    for i in positions:
        key = i.name
        value = i.average_position_price.value
        stocks[key] = float(value)

    return stocks

getStocks(TOKEN)