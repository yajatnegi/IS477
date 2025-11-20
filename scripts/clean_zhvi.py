import pandas as pd

def clean_zhvi(input_path="data/raw/ZHVI.csv", output_path="data/cleaned/ZHVI_cleaned.csv"):
    # Load raw Zillow data
    df = pd.read_csv(input_path)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Select useful columns
    keep_cols = ["regionid", "countyname", "state", "regiontype"] + [c for c in df.columns if c.startswith("20")]
    df = df[keep_cols]

    # Filter to county-level data
    df = df[df["regiontype"] == "county"]

    # Convert wide → long format
    df_long = df.melt(
        id_vars=["regionid", "countyname", "state"],
        var_name="date",
        value_name="zhvi"
    )

    # Drop rows with missing home values
    df_long = df_long.dropna(subset=["zhvi"])

    # Extract year
    df_long["year"] = df_long["date"].str[:4].astype(int)

    # Aggregate to annual median
    df_yearly = df_long.groupby(
        ["regionid", "countyname", "state", "year"],
        as_index=False
    )["zhvi"].median()

    # Save cleaned version
    df_yearly.to_csv(output_path, index=False)

    print(f"Cleaned ZHVI saved to {output_path}")


if __name__ == "__main__":
    clean_zhvi()

