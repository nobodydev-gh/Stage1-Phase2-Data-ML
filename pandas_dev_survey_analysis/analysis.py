import pandas as pd

df = pd.read_csv("/home/rohan/DEV/Stage1-Phase2-Data-ML/" \
"pandas_dev_survey_analysis/data/survey_results_public.csv")


print(df.head(10))



print(df.shape)


print(df.describe)


print(df.columns)

print(df.dropna(inplace=True),)


print(df.isna().sum().sort_values())


