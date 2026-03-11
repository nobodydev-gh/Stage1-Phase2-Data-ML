import pandas as pd

def merge_example():
    df1 = pd.DataFrame({'id': [1, 2], 'name': ['A', 'B']})
    df2 = pd.DataFrame({'id': [1, 2], 'salary': [100, 200]})
    return pd.merge(df1, df2, on='id')

def pivot_example():
    df = pd.DataFrame({
        'Country': ['India', 'India', 'USA'],
        'Salary': [100, 200, 300]
    })
    return pd.pivot_table(df, values='Salary', index='Country', aggfunc='mean')


if __name__ == "__main__":
    print(merge_example())
    print(pivot_example())