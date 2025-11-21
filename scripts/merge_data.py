'''
import pandas as pd

def merge_datasets(
    zhvi_path="data/cleaned/ZHVI_cleaned.csv",
    income_path="data/cleaned/Income_cleaned.csv",
    output_path="data/final/combined.csv"
):
    # Load cleaned datasets
    zhvi = pd.read_csv(zhvi_path)
    income = pd.read_csv(income_path)

    # Standardize column names
    zhvi.columns = zhvi.columns.str.lower()
    income.columns = income.columns.str.lower()

    # Rename regionid → fips (Zillow uses RegionID)
    if "regionid" in zhvi.columns:
        zhvi = zhvi.rename(columns={"regionid": "fips"})

    # Ensure FIPS is consistent type
    zhvi["fips"] = zhvi["fips"].astype(str)
    income["fips"] = income["fips"].astype(str)

    # Merge on (FIPS, year)
    merged = pd.merge(
        zhvi,
        income,
        on=["fips", "year"],
        how="inner"
    )

    # Save final dataset
    merged.to_csv(output_path, index=False)

    print(f"Merged dataset saved to {output_path}")


if __name__ == "__main__":
    merge_datasets()
'''
