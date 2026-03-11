import pandas as pd

def daily_high(df):
    df.set_index('Date', inplace=True)
    return df['High'].resample('D').max()

def weekly_summary(df):
    df.set_index('Date', inplace=True)
    return df[['Open', 'High', 'Low', 'Close']].resample('W').mean()


if __name__ == "__main__":
    df = pd.read_csv("data/ETH_1h.csv", parse_dates=['Date'])

    print(daily_high(df).head())