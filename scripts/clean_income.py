'''
import pandas as pd

def clean_income(input_path="data/raw/ERS_income.csv", output_path="data/cleaned/Income_cleaned.csv"):
    # Load USDA income dataset
    df = pd.read_csv(input_path)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Detect FIPS column (some datasets use different names)
    fips_col = None
    for col in df.columns:
        if "fips" in col:
            fips_col = col
            break

    if fips_col is None:
        raise ValueError("No FIPS column found in USDA dataset.")

    df = df.rename(columns={fips_col: "fips"})

    # Keep relevant columns (county, state, fips, year, income)
    income_cols = [c for c in df.columns if "median" in c or "income" in c]
    year_cols = [c for c in df.columns if c.isdigit()]

    # Convert wide → long
    df_long = df.melt(
        id_vars=["fips"],
        value_vars=year_cols,
        var_name="year",
        value_name="median_income"
    )

    # Clean formatting
    df_long["year"] = df_long["year"].astype(int)
    df_long = df_long.dropna(subset=["median_income"])

    # Save cleaned version
    df_long.to_csv(output_path, index=False)

    print(f"Cleaned income data saved to {output_path}")


if __name__ == "__main__":
    clean_income()
'''