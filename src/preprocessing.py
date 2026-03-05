import numpy as np
import pandas as pd

def compute_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute log returns from price series.
    """
    df = df.copy()
    df["log_return"] = (df["price"]/df["price"].shift(1)).apply(lambda x: np.log(x))
    df = df.dropna()
    return df