import pandas as pd

def filter_by_country(df, country):
    return df[df['Country'] == country]

def filter_multiple_countries(df, countries):
    return df[df['Country'].isin(countries)]

def filter_high_salary(df, threshold):
    return df[df['ConvertedCompYearly'] > threshold]


if __name__ == "__main__":
    df = pd.read_csv("data/survey_results_public.csv")

    india = filter_by_country(df, "India")
    print(india.head())

    high_paid = filter_high_salary(df, 100000)
    print(high_paid.head())