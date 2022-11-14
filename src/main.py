import os
import sys
import talib

from dotenv import load_dotenv
from binance import Client

# own module
from backtrader.Agent import Agent

load_dotenv()
client = Client(os.getenv('API_KEY'), os.getenv('API_SECRET'))


# Write your strategy here
if __name__ == '__main__':
    agent = Agent(100, 2, 1)
    # agent.print_detail()