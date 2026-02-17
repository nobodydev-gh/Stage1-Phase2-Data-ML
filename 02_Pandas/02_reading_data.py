import pandas as pd

# CSV
df = pd.read_csv('/home/rohan/DEV/' \
'Stage1-Phase2-Data-ML/02_Pandas/data/stack-overflow-developer-survey-2025/survey_results_public.csv')



print(df.head(2))

print("==================")
print(df.tail())
print(df.shape)
print(df.info())

# Excel
excel_df = pd.read_excel('data/coalpublic2013.xlsx')
print(excel_df.head())


