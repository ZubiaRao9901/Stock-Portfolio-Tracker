import yfinance as yf

# Define your stock portfolio
portfolio = {
    "AAPL": {"shares": 10, "purchase_price": 140},
    "GOOGL": {"shares": 5, "purchase_price": 120},
    "TSLA": {"shares": 8, "purchase_price": 700},
    "MSFT": {"shares": 12, "purchase_price": 250},
    "NVDA": {"shares": 15, "purchase_price": 400},
    "AMZN": {"shares": 7, "purchase_price": 100},
    "META": {"shares": 9, "purchase_price": 170},
    "NFLX": {"shares": 4, "purchase_price": 350},
    "AMD": {"shares": 20, "purchase_price": 110},
    "SOFI": {"shares": 25, "purchase_price": 8}
}

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return round(data["Close"].iloc[-1], 2)

# Show portfolio details
def display_portfolio(portfolio):
    print("\n📈 STOCK PORTFOLIO TRACKER 📊\n")
    total_investment = 0
    total_current_value = 0

    for symbol, info in portfolio.items():
        shares = info["shares"]
        buy_price = info["purchase_price"]
        current_price = get_current_price(symbol)
        investment = shares * buy_price
        current_value = shares * current_price
        profit = current_value - investment

        total_investment += investment
        total_current_value += current_value

        print(f"🔹 {symbol}")
        print(f"   Shares: {shares}")
        print(f"   Purchase Price: ${buy_price}")
        print(f"   Current Price: ${current_price}")
        print(f"   Invested: ${investment}")
        print(f"   Current Value: ${current_value}")
        print(f"   Profit/Loss: ${profit:.2f}\n")

    net_profit = total_current_value - total_investment
    print("💼 TOTAL SUMMARY:")
    print(f"   Total Investment: ${total_investment}")
    print(f"   Total Current Value: ${total_current_value}")
    print(f"   Net Profit/Loss: ${net_profit:.2f}")

# Run
display_portfolio(portfolio)
