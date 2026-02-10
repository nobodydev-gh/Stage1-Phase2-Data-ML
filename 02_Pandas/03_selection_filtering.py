import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')

print(df['Age'])
print(df.loc[0, 'Age'])

filt = df['Country'] == 'India'
print(df.loc[filt, 'Age'])

countries = ['India', 'Netherlands']
print(df[df['Country'].isin(countries)])
