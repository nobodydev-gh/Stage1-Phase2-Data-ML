import pandas as pd

df = pd.DataFrame({
    'Country':['India','India','USA'],
    'Salary':[100,200,300]
})

pivot = pd.pivot_table(df, values='Salary', index='Country', aggfunc='mean')
print(pivot)

print(pd.crosstab(df['Country'], df['Salary']))
