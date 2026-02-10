import pandas as pd
import numpy as np

# Sample Data
df = pd.DataFrame({
    'Country': ['India', 'India', 'USA', 'USA', 'UK', 'UK'],
    'Salary': [50000, 70000, 80000, 60000, 55000, 65000],
    'Experience': [2, 4, 5, 3, 2, 6]
})

print(df)

# -------------------------
# GROUPBY BASIC
group = df.groupby('Country')
print(group['Salary'].mean())

# -------------------------
# MULTIPLE AGGREGATIONS
print(group['Salary'].agg(['mean', 'median', 'count']))

# -------------------------
# MULTI-COLUMN AGG
print(group.agg({
    'Salary': ['mean', 'max'],
    'Experience': ['sum', 'min']
}))

# -------------------------
# APPLY CUSTOM FUNCTION
def exp_range(x):
    return x.max() - x.min()

print(group['Experience'].apply(exp_range))

# -------------------------
# PERCENTAGE CALCULATION
country_counts = df['Country'].value_counts()
salary_mean = group['Salary'].mean()

combined = pd.concat([country_counts, salary_mean], axis=1)
combined.columns = ['Total_Count', 'Avg_Salary']
print(combined)

# -------------------------
# RESAMPLING (TIME SERIES SAMPLE)
dates = pd.date_range('2024-01-01', periods=6)
ts_df = pd.DataFrame({'Date': dates, 'Sales': [10, 20, 15, 30, 25, 40]})
ts_df.set_index('Date', inplace=True)

print(ts_df.resample('2D').sum())

# -------------------------
# PIVOT TABLE
pivot = pd.pivot_table(df, values='Salary', index='Country', aggfunc='mean')
print(pivot)

# -------------------------
# CROSSTAB
print(pd.crosstab(df['Country'], df['Experience']))
