import yfinance as yf


def get_asia_tech_exposure(tickers):
    exposure_data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        if len(hist) >= 2:
            yesterday = hist.iloc[-2]['Close']
            today = hist.iloc[-1]['Close']
            change_pct = round(((today - yesterday) / yesterday) * 100, 2)
            exposure_data[ticker] = {
                'yesterday': yesterday,
                'today': today,
                'change_pct': change_pct
            }
    return exposure_data
# Fetch market data using yfinance
# Fetch market data using yfinance
