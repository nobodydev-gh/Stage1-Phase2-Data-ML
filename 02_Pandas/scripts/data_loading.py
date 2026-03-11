import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def load_excel(path):
    return pd.read_excel(path)


if __name__ == "__main__":
    df = load_csv("data/survey_results_public.csv")
    print(df.head())
    print("Shape:", df.shape)