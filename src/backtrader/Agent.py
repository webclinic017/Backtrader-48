import pandas as pd
from backtrader import Orderer
from backtrader import Analyzer


class Agent:
    def __init__(self, asset, leverage, commission, dataframe):
        self.asset = asset
        self.leverage = leverage
        self.commission = commission / 100
        self.dataframe = dataframe

        self.holding = 0

        self.orderer = Orderer.Orderer(
            self.asset, self.commission, self.leverage)
        self.analyzer = Analyzer.Analyzer(self.dataframe)

    def open_long_position(self, idx, amount):
        print('Open long position.')
        self.analyzer.record_open(self.asset, idx)

        self.asset, self.holding = self.orderer.open_long_position(
            self.dataframe['Close'][idx], amount)

    def close_long_position(self, idx, amount):
        print('Close long position.')
        self.asset, self.holding = self.orderer.close_long_position(
            self.dataframe['Close'][idx], amount)

        self.analyzer.record_close(self.asset, idx)

    def open_short_position(self, idx, amount):
        print('Open short position.')
        self.analyzer.record_open(self.asset, idx)

        self.asset, self.holding = self.orderer.open_short_position(
            self.dataframe['Close'][idx], amount)

    def close_short_position(self, idx, amount):
        print('Close short position.')
        self.asset, self.holding = self.orderer.close_short_position(
            self.dataframe['Close'][idx], amount)

        self.analyzer.record_close(self.asset, idx)

    def log(self, price):
        self.analyzer.record_log(self.asset, self.holding, price)
        print('asset:', self.asset + self.holding * price)
        print('holding:', self.holding)
        print()

    def analyze(self):
        self.analyzer.analysis()

    def fill_unuse_place(self, end):
        self.analyzer.fill_unuse_place(end, self.asset)
        
    def print_agent_detail(self):
        print('asset:', self.asset)
        print('leverage:', self.leverage)
        print('commission:', self.commission)


if __name__ == '__main__':
    df = [100, 200, 3]
    df = pd.DataFrame(df)

    agent = Agent(100, 2, 1, df)
    agent.open_long_position(100, 1)
    agent.log(100)
    agent.close_long_position(200, 1)
    agent.log(200)

    # agent.analyzer.log_detail()
    # agent.analyze()
