import yfinance as yf
import matplotlib.pyplot as plt

symbols = ['EURUSD=X', 'JPM']

data = {symbol: yf.download(symbol, start="2020-01-01", end="2025-10-01") for symbol in symbols}

for symbol, df in data.items():
    df.to_csv(f"data/{symbol}.csv")

# ---------- Raccolta dati ------------ #
for symbol, df in data.items():
    # Media mobile a 7 giorni: trend a breve periodo
    df['MA_7'] = df['Close'].rolling(window=7).mean()

    # Media mobile a 30 giorni: trend a lungo periodo
    df['MA_30'] = df['Close'].rolling(window=30).mean()

    # Volatilità a 7 giorni: deviazione standard dei prezzi di chiusura
    df['Volatility'] = df['Close'].rolling(window=7).std()

    # Variazione percentuale giornaliera dei prezzi di chiusura
    df['Daily Change (%)'] = df['Close'].pct_change() * 100



# ---------- Grafici ------------ #
for symbol, df in data.items():
    # Prezzo e media mobili
    plt.figure(figsize=(12, 6))

    plt.plot(df['Close'], label='Chiusura', linewidth=1)
    plt.plot(df['MA_7'], label='MA 7 giorni', linestyle='--')
    plt.plot(df['MA_30'], label='MA 30 giorni', linestyle=':')

    plt.title(f"{symbol} - Prezzo e Medie Mobili")
    plt.xlabel('Data')
    plt.ylabel('Prezzo ($)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/{symbol}_trend.png")
    plt.close()

    # Variazione percentuale giornaliera
    plt.figure(figsize=(12, 6))
    plt.plot(df['Daily Change (%)'], color='orange', label='Variazione giornaliera (%)')
    plt.title(f"{symbol} - Variazione percentuale giornaliera")
    plt.xlabel('Data')
    plt.ylabel('Variazione (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/{symbol}_daily_change.png")
    plt.close()

    # Volatilità
    plt.figure(figsize=(12, 6))
    plt.plot(df['Volatility'], color='red', label='Volatilità a 7 giorni')
    plt.title(f"{symbol} - Volatilità settimanale")
    plt.xlabel('Data')
    plt.ylabel('Volatilità ($)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/{symbol}_volatility.png")
    plt.close()

