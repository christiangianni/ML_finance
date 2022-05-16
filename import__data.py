# This is a sample Python script.

import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
plt.show()


def import_from_yfinance(name):
    # Use a breakpoint in the code line below to debug your script.
    aapl_df = yf.download(name,
                          start='2019-01-01',
                          end='2021-06-12',
                          progress=False,
                          )
    aapl_df.head()
    print(aapl_df.head())
    ticker = yf.Ticker('AAPL')
    aapl_df = ticker.history(period="1mo")  #valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    aapl_df['Close'].plot(title="APPLE's stock price")
    print(ticker.recommendations)
    print(ticker.dividends)
    print(ticker.earnings)



    print('0')


def import_from_yahoo_financials(name):
    # Use a breakpoint in the code line below to debug your script.
    yahoo_financials = YahooFinancials(name)
    data = yahoo_financials.get_historical_price_data(start_date='2019-01-01',
                                                      end_date='2019-12-31',
                                                      time_interval='weekly')
    aapl_df = pd.DataFrame(data['AAPL']['prices'])
    aapl_df = aapl_df.drop('date', axis=1).set_index('formatted_date')
    aapl_df.head()
    print(aapl_df.head())


def test_plot():
    plt.show()
    time = [0, 1, 2, 3]
    position = [0, 100, 200, 300]

    plt.plot(time, position)
    plt.xlabel('Time (hr)')
    plt.ylabel('Position (km)')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import_from_yfinance('AAPL')
    #import_from_yahoo_financials('AAPL')
    #test_plot()
    plt.show()
    print('1')