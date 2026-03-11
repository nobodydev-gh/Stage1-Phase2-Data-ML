import pandas as pd

def export_india_data(df):
    india = df[df['Country'] == 'India']
    india.to_csv("data/india.csv", index=False)
    india.to_json("data/india.json", orient='records', lines=True)


if __name__ == "__main__":
    df = pd.read_csv("data/survey_results_public.csv")
    export_india_data(df)
    print("Exported successfully.")