import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns

# own module
from backtrader import Plotter

class Analyzer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

        self.open_change = False
        self.close_change = False
        
        self.profit = 0

        self.open_asset = 0

        self.win_order = 0
        self.loss_order = 0

        self.win_money = 0
        self.loss_money = 0

        self.plotter = Plotter.Plotter(self.dataframe, 0.005)
        
    def record_open(self, asset, idx):
        self.open_asset = asset

        self.plotter.add_open_place(self.dataframe['Low'][idx]*0.995)
        self.open_change = True

    def record_close(self, asset, idx):
        if (asset > self.open_asset):
            self.win_order += 1
            self.win_money += asset - self.open_asset
        else:
            self.loss_order += 1
            self.loss_money += self.open_asset - asset

        self.plotter.add_close_place(self.dataframe['High'][idx])
        self.close_change = True

    def record_log(self, asset, holding, price):
        self.plotter.add_asset_change(asset + holding * price)

        if not self.open_change:
            self.plotter.add_open_place(np.nan)
        else:
            self.open_change = False
            
        if not self.close_change:
            self.plotter.add_close_place(np.nan)
        else:
            self.close_change = False

    def analysis(self):
        print('win order:', self.win_order)
        print('loss_order:', self.loss_order)
        print('win rate:', self.__calculate_rate(
            self.win_money, self.loss_money))

        print('win money:', self.win_money)
        print('loss money:', self.loss_money)
        print('earn rate:', self.__calculate_rate(
            self.win_money, self.loss_money))

        # add_plot = [mpf.make_addplot(self.asset_change, type='line', color='black'),
        #             mpf.make_addplot(self.open_place, type='scatter', marker='^', markersize=100),
        #             mpf.make_addplot(self.close_place, type='scatter', marker='v', markersize=100)
        #             ]
        
        # self.test_plot.append(mpf.make_addplot(self.asset_change, type='line', color='black'))
        
        # mpf.dataframe(self.dataframe, type='candle', style='binance', addplot=self.test_plot, main_panel=0, volume=True)
        # plt.show()
        self.plotter.plot()

    def log_detail(self):
        print('win order:', self.win_order)
        print('loss order:', self.loss_order)

        print('win money:', self.win_money)
        print('loss money:', self.loss_money)


    def fill_unuse_place(self, end, asset):
        self.plotter.fill_unuse_place(end, asset)
            
    @staticmethod
    def __calculate_rate(win, loss):
        return win / (win + loss)
