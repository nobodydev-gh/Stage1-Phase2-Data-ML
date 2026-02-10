import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')

group = df.groupby('Country')
print(group['ConvertedCompYearly'].median().loc['India'])

print(group['ConvertedCompYearly'].agg(['median','count']))
