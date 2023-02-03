apikey = "pMynOXuLSTBMzvSntePiycX3v4tNJ7DABVDpkLK5xkin2uw0NLSyImwj2at5nn7M"
secret = "lIo9OcJyTFrCdqoqo9YxnJzs1m2CFgEcSZOcLGcHCGzHsejOEB191WXhe6VuVwQ8"
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd


client = Client(apikey, secret)
tickers = client.get_all_tickers()
ticker_df = pd.DataFrame(tickers)
ticker_df.set_index("symbol", inplace=True)

# print(ticker_df.loc["BTCUSDT"])
depth = client.get_order_book(symbol="ETHBTC")
depth_df = pd.DataFrame(depth["bids"])
depth_df.columns = ["Price", "Volume"]
# print(depth_df)
historical = client.get_historical_klines(
    "ETHBTC", client.KLINE_INTERVAL_1DAY, "19 Oct 2021"
)
print(historical)
hist_df = pd.DataFrame(historical)
print(hist_df)
hist_df.columns = [
    "Open time",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Close time",
    "Quote Asset Volume",
    "Number of Trades",
    "TB Base Volume",
    "TB Quote Volume",
    "Ignore",
]
print(hist_df)
print(hist_df.dtypes)
hist_df["Open time"] = pd.to_datetime(hist_df["Open time"] / 1000, unit="s")
hist_df["Close time"] = pd.to_datetime(hist_df["Close time"] / 1000, unit="s")
print(hist_df.dtypes)
print(hist_df)
numeric_columns = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Quote Asset Volume",
    "TB Base Volume",
    "TB Quote Volume",
]
hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)
print(hist_df.dtypes)
print(hist_df.info())
import mplfinance as mpf

mpf.plot(
    hist_df.set_index("Close time").tail(100),
    type="candle",
    style="charles",
    volume=True,
    title="ETHBTC Last 100 Days",
    mav=(10, 20),
)
