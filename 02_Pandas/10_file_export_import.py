import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')

india = df[df['Country'] == 'India']

india.to_csv('data/india.csv')
india.to_json('data/india.json')

test = pd.read_json('data/india.json')
print(test.head())
