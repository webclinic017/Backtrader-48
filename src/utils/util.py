import os
import pandas as pd

from dotenv import load_dotenv
from binance import Client

load_dotenv()
client = Client(os.getenv('API_KEY'), os.getenv('API_SECRET'))

def build_dataframe(symbol, interval, look_back):
    frame = pd.DataFrame(columns=range(6))
    frame = pd.DataFrame(client.futures_historical_klines(
        symbol, interval, look_back + ' ago UTC'))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index+28800000, unit='ms')
    frame = frame.astype(float)
    return frame
