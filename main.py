# This is a sample Python script.

import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


def import_from_y(name):
    # Use a breakpoint in the code line below to debug your script.
    aapl_df = yf.download('AAPL',
                          start='2019-01-01',
                          end='2021-06-12',
                          progress=False,
                          )
    aapl_df.head()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
