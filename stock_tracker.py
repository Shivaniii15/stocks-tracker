import requests
# -----------------------------
# CONFIG (fill later)
# -----------------------------
STOCKS = ["AAPL", "GOOGL", "TSLA"]

BUY_PRICES = {
    "AAPL": 150.0,
    "GOOGL": 2500.0,
    "TSLA": 700.0
}

API_URL = "https://api.example.com/stock"  # replace later


# -----------------------------
# FETCH PRICE (placeholder)
# -----------------------------
def get_stock_price(symbol):
    """
    Replace this with real API logic later.
    """
    # TODO: connect to real API
    # response = requests.get(f"{API_URL}?symbol={symbol}")
    # data = response.json()
    # return data["price"]

    return 0  # placeholder


# -----------------------------
# CALCULATE P/L
# -----------------------------
def calculate_profit_loss(symbol, current_price):
    buy_price = BUY_PRICES[symbol]
    return current_price - buy_price


# -----------------------------
# MAIN LOGIC
# -----------------------------
def main():
    print("Stock Tracker Running...\n")

    for stock in STOCKS:
        current_price = get_stock_price(stock)
        pnl = calculate_profit_loss(stock, current_price)

        print(f"{stock}: Current Price = {current_price}, P/L = {pnl}")


if __name__ == "__main__":
    main()