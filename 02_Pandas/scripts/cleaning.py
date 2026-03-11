import pandas as pd
import numpy as np

def clean_yearscode(df):
    df['YearsCode'] = df['YearsCode'].replace({
        "Less than 1 year": 0,
        "More than 50 years": 50
    })
    df['YearsCode'] = pd.to_numeric(df['YearsCode'], errors='coerce')
    return df

def remove_missing_salary(df):
    return df.dropna(subset=['ConvertedCompYearly'])

def detect_outliers(df):
    q1 = df['ConvertedCompYearly'].quantile(0.25)
    q3 = df['ConvertedCompYearly'].quantile(0.75)
    iqr = q3 - q1

    return df[
        (df['ConvertedCompYearly'] < q1 - 1.5 * iqr) |
        (df['ConvertedCompYearly'] > q3 + 1.5 * iqr)
    ]


if __name__ == "__main__":
    df = pd.read_csv("data/survey_results_public.csv")

    df = clean_yearscode(df)
    df = remove_missing_salary(df)

    outliers = detect_outliers(df)
    print("Outliers:")
    print(outliers.head())