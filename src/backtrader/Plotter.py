import numpy as np
import pandas as pd
import seaborn as sns
import mplfinance as mpf
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, dataframe, distance):
        self.dataframe = dataframe

        self.main_plot = []

        self.marker_distance = distance
        self.open_place = []
        self.close_place = []

        self.asset_change = []

    # fast set class members
    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

    def set_main_plot(self, dataframe):
        self.main_plot = dataframe

    def set_marker_distance(self, dis):
        self.marker_distance = dis

    def set_open_place(self, dataframe):
        self.open_place = dataframe

    def set_close_place(self, dataframe):
        self.close_place = dataframe

    def set_asset_change(self, dataframe):
        self.asset_change = dataframe

    def reset_all(self):
        self.main_plot = []
        self.asset_change = []
        self.open_place = []
        self.close_place = []

    # interface methods
    def add_open_place(self, data):
        self.open_place.append(data * (1 - self.marker_distance))

    def add_close_place(self, data):
        self.close_place.append(data * (1 + self.marker_distance))

    def add_asset_change(self, data):
        self.asset_change.append(data)

    def fill_unuse_place(self, end, asset):
        for i in range(0, end):
            self.asset_change.append(asset)
            self.open_place.append(np.nan)
            self.close_place.append(np.nan)

    def plot(self):
        self.main_plot.append(mpf.make_addplot(
            self.asset_change, type='line', color='black'))
        self.main_plot.append(mpf.make_addplot(
            self.open_place, type='scatter', marker='^', markersize=100))
        self.main_plot.append(mpf.make_addplot(
            self.close_place, type='scatter', marker='v', markersize=100))

        mpf.plot(self.dataframe, type='candle', style='binance',
                 addplot=self.main_plot, main_panel=0, volume=True)
        plt.show()
