# scripts/prepare_data.py

import pandas as pd
import numpy as np
from pathlib import Path

RAW_DIR = Path("data/raw")
INTERIM_DIR = Path("data/interim")
PROCESSED_DIR = Path("data/processed")

INTERIM_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_zillow():
    zillow_path = RAW_DIR / "zillow_zhvi_county.csv"
    z = pd.read_csv(zillow_path)
    z = z[["RegionName", "State", "StateCodeFIPS", "MunicipalCodeFIPS", "2022-12-31"]].copy()
    z.rename(columns={"2022-12-31": "ZHVI_2022"}, inplace=True)
    z["FIPS_str"] = (
        z["StateCodeFIPS"].astype(int).astype(str).str.zfill(2)
        + z["MunicipalCodeFIPS"].astype(int).astype(str).str.zfill(3)
    )
    z = z.dropna(subset=["ZHVI_2022"])
    return z

def load_usda():
    usda_path = RAW_DIR / "usda_median_income_county.csv"
    u = pd.read_csv(usda_path)
    u = u[u["Attribute"] == "Median_Household_Income_2022"].copy()
    u["FIPS_str"] = u["FIPS_Code"].apply(
        lambda x: str(int(x)).zfill(5) if not pd.isna(x) else np.nan
    )
    u = u[u["FIPS_str"].str.len() == 5]
    u.rename(columns={"Value": "Median_Income_2022"}, inplace=True)
    return u

def main():
    z = load_zillow()
    u = load_usda()

    z.to_csv(INTERIM_DIR / "zillow_2022_clean.csv", index=False)
    u.to_csv(INTERIM_DIR / "usda_income_2022_clean.csv", index=False)

    merged = z.merge(
        u[["FIPS_str", "Area_Name", "Median_Income_2022"]],
        on="FIPS_str",
        how="inner",
        validate="many_to_one"
    )

    merged = merged[(merged["Median_Income_2022"] > 0) & (merged["ZHVI_2022"] > 0)]

    out_path = PROCESSED_DIR / "county_housing_income_2022.csv"
    merged.to_csv(out_path, index=False)
    print(f"Saved merged dataset to {out_path}")
    print(f"Shape: {merged.shape}")

if __name__ == "__main__":
    main()
