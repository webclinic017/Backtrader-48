import pandas as pd

from Orderer import Orderer
from Analyzer import Analyzer


class Agent:
    def __init__(self, asset, leverage, commission, dataframe):
        self.asset = asset
        self.leverage = leverage
        self.commission = commission / 100
        self.dataframe = dataframe

        self.holding = 0

        self.orderer = Orderer(self.asset, self.commission, self.leverage)
        self.analyzer = Analyzer(self.dataframe)

    def open_long_position(self, price, amount):
        print('Open long position.')
        self.asset, self.holding = self.orderer.open_long_position(
            price, amount)

        self.analyzer.record_open(price)

    def close_long_position(self, price, amount):
        print('Close long position.')
        self.asset, self.holding = self.orderer.close_long_position(
            price, amount)

        self.analyzer.record_close(price)

    def open_short_position(self, price, amount):
        print('Open short position.')
        self.asset, self.holding = self.orderer.open_short_position(
            price, amount)

        self.analyzer.record_open(price)

    def close_short_position(self, price, amount):
        print('Close short position.')
        self.asset, self.holding = self.orderer.close_short_position(
            price, amount)

        self.analyzer.record_close(price)

    def log(self, price):
        self.analyzer.record_log(self.asset, self.holding, price)
        print('asset:', self.asset + self.holding * price)
        print('holding:', self.holding)

    def print_agent_detail(self):
        print('asset:', self.asset)
        print('leverage:', self.leverage)
        print('commission:', self.commission)


if __name__ == '__main__':
    df = [1, 2, 3]
    df = pd.DataFrame(df)

    agent = Agent(100, 2, 1, df)
    agent.open_long_position(100, 1)
    agent.log(100)
