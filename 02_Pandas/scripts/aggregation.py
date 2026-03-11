import pandas as pd

def country_salary_stats(df):
    return df.groupby('Country')['ConvertedCompYearly'].agg(['median', 'mean', 'count'])

def multi_column_aggregation(df):
    return df.groupby('Country').agg(
        median_salary=('ConvertedCompYearly', 'median'),
        avg_salary=('ConvertedCompYearly', 'mean'),
        respondents=('ConvertedCompYearly', 'count')
    )

def salary_experience_correlation(df):
    return df[['YearsCode', 'ConvertedCompYearly']].corr()


if __name__ == "__main__":
    df = pd.read_csv("data/survey_results_public.csv")

    stats = country_salary_stats(df)
    print(stats.sort_values(by='count', ascending=False).head(10))

    print("\nCorrelation:")
    print(salary_experience_correlation(df))