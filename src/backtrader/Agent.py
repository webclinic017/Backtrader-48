class Agent:
    def __init__(self, asset, leverage, commission):
        self.asset = asset
        self.leverage = leverage
        self.commission = commission
    
    def print_detail(self):
        print('asset:', self.asset)
        print('leverage:', self.leverage)
        print('commission:', self.commission)