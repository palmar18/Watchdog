import yfinance as yf

def monitor_market(ticker="TSLA"):
    print(f"Checking {ticker}...")
    data = yf.download(ticker, period="2d", interval="1h")
    latest = data['Close'].iloc[-1]
    prev = data['Close'].iloc[0]
    change = ((latest - prev) / prev) * 100

    print(f"{ticker} current: ${latest:.2f} | Change: {change:.2f}%")

    if change < -10:
        print("🚨 ALERT: Price dropped more than 10%! Potential opportunity.")
