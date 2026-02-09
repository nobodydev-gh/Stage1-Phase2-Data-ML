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
