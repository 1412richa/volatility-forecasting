import yfinance as yf
import pandas as pd

def download_price_data(ticker: str, start: str = "2000-01-01") -> pd.Dataframe:
    """
    Download historical price data from Yahoo Finance.

    Parameters
    ----------
    ticker : str
        Ticker symbol (eg '^GSPC' for S&P 500, '^VIX' for VIX)
    start : str
        Start date for historical data

    Returns
    -------
    pd.Dataframe
        Clean dataframe with Date index and Adjusted Close column
    """

    data = yf.download(ticker, start=start, progress=False)

    df = data[["Adj Close"]].copy()
    df.rename(columns={"Adj Close": "price"}, inplace=True)

    df.index = pd.to_datetime(df.index)

    return df