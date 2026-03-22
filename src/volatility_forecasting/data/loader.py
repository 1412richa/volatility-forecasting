import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path.cwd().parent.absolute().joinpath("data")

def download_price_data(ticker: str, start: str = "2000-01-01") -> pd.DataFrame:
    """
    Download historical price data from Yahoo Finance or load from cache if available.

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
    DATA_DIR.mkdir(exist_ok=True)

    safe_ticker = ticker.replace("^", "")
    file_path = DATA_DIR / f"{safe_ticker}.csv"

    # Load cached data if it exists
    if file_path.exists():
        df = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    else:
        df = yf.download(ticker, start=start, progress=False)

        # Handle multiindex columns
        if isinstance(df.columns, pd.MultiIndex):
            df = df.xs(ticker, axis=1, level=1)

        # Prefer adjusted price if available, otherwise use close price
        price_col = "Adj Close" if "Adj Close" in df.columns else "Close"
        df = df[[price_col]]
        df.rename(columns={price_col: "price"}, inplace=True)

        # Reindex to frequency and sort by date
        df = pd.to_datetime(df.index)
        df.index.freq = pd.infer_freq(df.index)
        # df = df.asfreq("B").sort_index()

        df.to_csv(file_path)


    return df