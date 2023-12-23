import yfinance as yf
import sys

if len(sys.argv) > 1:
    yf.set_proxy_url(sys.argv[1])

data = yf.download("AAPL",start="2023-12-01")
print(data)
print(len(data))
