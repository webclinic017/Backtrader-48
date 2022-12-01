import os
import talib

import pandas as pd

# own module
from backtrader.Agent import Agent
from utils import util

# Write your strategy here
if __name__ == '__main__':
    df = util.build_dataframe('ETHBUSD', '15m', '1 weeks')
    agent = Agent(100, 2, 1, df)

    slowk, slowd = talib.STOCH(
        df['High'], df['Low'], df['Close'], fastk_period=9, slowk_period=5, slowd_period=4)

    print('---------- Backtest Started ----------')
    start = util.get_efficient_start(slowk)
    agent.fill_unuse_place(start)
    for idx in range(start, len(df['Close'])):
        if agent.holding == 0:
            if slowk[idx] > slowd[idx] and slowk[idx-1] < slowd[idx-1]:
                agent.open_long_position(idx, 0.99)

            elif slowk[idx] < slowd[idx] and slowk[idx-1] > slowd[idx-1]:
                agent.open_short_position(idx, 0.99)

        elif agent.holding > 0:
            if slowk[idx] < slowd[idx] and slowk[idx-1] > slowd[idx-1]:
                agent.close_long_position(idx, 1)
                agent.open_short_position(idx, 0.99)

        elif agent.holding < 0:
            if slowk[idx] > slowd[idx] and slowk[idx-1] < slowd[idx-1]:
                agent.close_short_position(idx, 1)
                agent.open_long_position(idx, 0.99)

        print('k: ', slowk[idx])
        print('d: ', slowd[idx])
        print('price:', df['Close'][idx])
        agent.log(df['Close'][idx])

    agent.analyze()
