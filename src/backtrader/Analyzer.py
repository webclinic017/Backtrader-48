import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

class Analyzer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

        self.holding_change = False
        self.profit = 0

        self.open_asset = 0

        self.win_order = 0
        self.loss_order = 0

        self.win_money = 0
        self.loss_money = 0

        self.open_place = []
        self.close_place = []
        self.asset_change = []

    def record_open(self, price):
        self.open_place.append(price*0.95)
        self.close_place.append(np.nan)
        self.holding_change = True

    def record_close(self, price):
        self.open_place.append(np.nan)
        self.close_place.append(price*0.95)
        self.holding_change = True

    def record_log(self, asset, holding, price):
        self.asset_change.append(asset + holding * price)

        if self.holding_change:
            self.holding_change = False

        else:
            self.open_place.append(np.nan)
            self.close_place.append(np.nan)

    def analysis(self):
        print('win order:', self.win_order)
        print('loss_order:', self.loss_order)
        print('win rate:', self.__calculate_rate(
            self.win_money, self.loss_money))

        print('win money:', self.win_money)
        print('loss money:', self.loss_money)
        print('earn rate:', self.__calculate_rate(
            self.win_money, self.loss_money))

        add_plot = [mplfinance.make_addplot(self.asset_change, type='line', panel=1),
                    mpf.make_addplot(self.buy_place, type='scatter',
                                     marker='^', markersize=100),
                    mpf.make_addplot(self.sell_place, type='scatter', marker='v', markersize=100)]

        plt.plot(self.asset_change)
        plt.show()

    def __calculate_rate(win, loss):
        return win / (win + loss)


if __name__ == '__main__':
    df = [1, 2, 3]
    df = pd.DataFrame(df)
    analyzer = Analyzer(df)
    
    analyzer.analysis()
