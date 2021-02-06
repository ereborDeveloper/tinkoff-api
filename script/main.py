import tinvest


def getStocks():
    stocks = {}
    client = tinvest.SyncClient(TOKEN)
    response = client.get_portfolio()
    positions = response.payload.positions

    for i in positions:
        key = i.name
        value = i.average_position_price.value
        stocks[key] = float(value)

    return stocks