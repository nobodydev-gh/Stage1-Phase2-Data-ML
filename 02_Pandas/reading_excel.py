import pandas as pd
import openpyxl

df = pd.read_excel('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/coalpublic2013.xlsx')

print(df)

print(df.head())


print(df.tail())

print(df.describe())