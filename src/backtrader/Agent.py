from Orderer import Orderer
from Analyzer import Analyzer

class Agent:
    def __init__(self, asset, leverage, commission):
        self.asset = asset
        self.leverage = leverage
        self.commission = commission

        self.orderer = Orderer()
        self.analyzer = Analyzer()

    def open_long_position(self):
        print('Open long position.')
        self.orderer.buy()

    def close_long_position(self):
        print('Close long position.')
        self.orderer.sell()

    def open_short_position(self):
        print('Open short position.')
        self.orderer.sell()

    def close_short_position(self):
        print('Close short position.')
        self.orderer.buy()

    def log(self):
        self.analyzer.log()

    def print_agent_detail(self):
        print('asset:', self.asset)
        print('leverage:', self.leverage)
        print('commission:', self.commission)


if __name__ == '__main__':
    agent = Agent(100, 2, 1)
    
    agent.log()