import yfinance as yf
import pandas as pd

# Esempio: EUR/USD e titolo bancario (es. JPMorgan)
symbols = ['EURUSD=X', 'JPM']

data = {symbol: yf.download(symbol, start="2020-01-01", end="2025-01-01") for symbol in symbols}

# Salva i dati grezzi
for symbol, df in data.items():
    df.to_csv(f"data/{symbol}.csv")

for symbol, df in data.items():
    df['MA_7'] = df['Close'].rolling(window=7).mean()
    df['MA_30'] = df['Close'].rolling(window=30).mean()
    df['Volatility'] = df['Close'].rolling(window=7).std()
    df['Daily Change (%)'] = df['Close'].pct_change() * 100
