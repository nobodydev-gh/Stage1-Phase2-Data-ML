import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')

df.sort_values(by='WorkExp', ascending=False, inplace=True)
print(df.head())

df.set_index('ResponseId', inplace=True)
print(df.iloc[0])

df.reset_index(inplace=True)
