# Volatility Forecasting & Model Validation in Equity Markets

## Objective
Forecast and compare volatility models (ARIMA, GARCH, ML) on S&P 500 returns.

## Data
- S&P 500 (Yahoo Finance)
- VIX (Yahoo Finance)

## Project Structure
- `data/` -> raw and processed data
- `notebooks/` -> exploratory and modeling notebooks
- `src/` -> reusable scripts (loading, preprocessing, models)
- `README.md` -> project overview
- `requirements.txt` -> Python packages

## Methodology
1. Data cleaning & exploration
2. Log return calculation
3. Stationarity & autocorrelation analysis
4. ARIMA modeling
5. GARCH modeling
6. Walk-forward backtesting
7. Comparison & discussion

## Key Insights
Under Construction

## Environment Setup
```bash
git clone
https://github.com/1412richa/volatility-forecasting.git
cd volatility-forecasting

python -m venv .venv
source venv\Scripts\activate

pip install -r requirements.txt
```