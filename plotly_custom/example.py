import yfinance as yf
from plotly_custom import scatter

msft = yf.Ticker("MSFT")
hist = msft.history(period="max")
hist.drop('Volume', axis=1, inplace=True)

fig = scatter(data=hist)
fig.set_dropdown(True)
fig.show()