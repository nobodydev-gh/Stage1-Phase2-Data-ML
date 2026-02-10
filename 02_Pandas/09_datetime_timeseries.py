import pandas as pd

df = pd.read_csv('data/ETH_1h.csv', parse_dates=['Date'])

df.set_index('Date', inplace=True)
print(df['2020-01':'2020-02'])

daily_high = df['High'].resample('D').max()
print(daily_high.head())
