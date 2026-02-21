import pandas as pd

def create_sample_dataframe():
    data = {
        'first': ['Rohan', 'Hema', 'Ravi'],
        'last': ['Kumar', 'Sharma', 'Singh'],
        'age': [21, 22, 23]
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = create_sample_dataframe()

    print("DataFrame:")
    print(df)

    print("\nSelect column:")
    print(df['first'])

    print("\nMultiple columns:")
    print(df[['first', 'age']])

    print("\nUsing iloc:")
    print(df.iloc[0])

    print("\nUsing loc:")
    print(df.loc[0, 'first'])