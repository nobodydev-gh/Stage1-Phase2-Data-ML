import pandas as pd
import datetime

# d_parser = lambda x : pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
date_format= '%Y-%m-%d %I-%p'
df=pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/ETH_1h.csv', parse_dates=['Date'],date_format=date_format)

print(df.head(10))

print(df.shape)

print("------")

print(df.describe)


print(df.loc[0,'Date'])

df["Date"] = pd.to_datetime(df['Date'],format='%Y-%m-%d %I-%p')
print(df['Date'])


print(df.loc[0, 'Date'].day_name())  ## for single


print(df['Date'].dt.day_name())  # for entire series

## add day for each row

df["Dateofweek"] = df['Date'].dt.day_name()

print(df)


print(df['Date'].max())


##we can also get  a time delta by subtracting

print(df['Date'].max() - df['Date'].min())


filt = (df['Date'] >= '2019')  & (df['Date'] <= '2020')

print(df.loc[filt])


filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[filt]




df.set_index('Date', inplace=True)


print("\n")
print(df)


print(df.loc['2019'])

df.sort_index(inplace=True)
print(df['2020-01':'2020-02'])


print(df['2020-01':'2020-02']['Close'].mean())


print(df.loc['2020-01-01']['High'].max())



highs = df['High'].resample('D').max()
print(highs.loc['2020-01-01'])




import matplotlib_inline

print(highs.plot())

print(df[['Open', 'High','Low', 'Close', 'Volume']].resample('W').mean())

print("---------------------------")
stats=df[['Open', 'High','Low', 'Close', 'Volume']].resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
print(stats)



