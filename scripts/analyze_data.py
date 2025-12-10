import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
FIG_DIR = Path("figures")

FIG_DIR.mkdir(parents=True, exist_ok=True)

def main():
    data_path = PROCESSED_DIR / "county_housing_income_2022.csv"
    df = pd.read_csv(data_path)

    # Summary stats
    summary = df[["ZHVI_2022", "Median_Income_2022"]].describe()
    corr = df[["ZHVI_2022", "Median_Income_2022"]].corr().iloc[0, 1]

    print("Summary statistics:")
    print(summary)
    print("\nPearson correlation between ZHVI_2022 and Median_Income_2022:")
    print(corr)

    # Save summary + correlation to CSV / TXT for reproducibility
    summary.to_csv(PROCESSED_DIR / "summary_stats_2022.csv")
    with open(PROCESSED_DIR / "correlation_2022.txt", "w") as f:
        f.write(f"Pearson correlation: {corr:.4f}\n")

    slope, intercept = np.polyfit(df["Median_Income_2022"], df["ZHVI_2022"], 1)
    with open(PROCESSED_DIR / "regression_2022.txt", "w") as f:
        f.write(f"ZHVI_2022 ≈ {intercept:.2f} + {slope:.4f} * Median_Income_2022\n")


    # Scatter plot (log-scale on ZHVI to reduce skew)
    plt.figure()
    plt.scatter(df["Median_Income_2022"], df["ZHVI_2022"], alpha=0.3)
    plt.xlabel("Median Household Income, 2022 (USD)")
    plt.ylabel("ZHVI, December 2022 (USD)")
    plt.title("County-Level Income vs. Home Values (2022)")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "income_vs_zhvi_scatter.png", dpi=200)

    # Optionally log transform ZHVI for a cleaner plot
    plt.figure()
    plt.scatter(df["Median_Income_2022"], np.log(df["ZHVI_2022"]), alpha=0.3)
    plt.xlabel("Median Household Income, 2022 (USD)")
    plt.ylabel("log(ZHVI_2022)")
    plt.title("Income vs. log(Home Values) (2022)")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "income_vs_log_zhvi_scatter.png", dpi=200)

if __name__ == "__main__":
    main()