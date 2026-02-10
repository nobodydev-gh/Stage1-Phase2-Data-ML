import pandas as pd

# CSV
df = pd.read_csv('data/survey_results_public.csv')
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())

# Excel
excel_df = pd.read_excel('data/coalpublic2013.xlsx')
print(excel_df.head())
