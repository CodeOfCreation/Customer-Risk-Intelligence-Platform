from pathlib import Path

import pandas as pd
from ydata_profiling import ProfileReport


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "IBM_Customer_Churn.csv"
REPORT_PATH = PROJECT_ROOT / "reports" / "IBM_Customer_Churn_profile.html"


def main() -> None:
    print(f"Loading dataset: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    profile = ProfileReport(
        df,
        title="IBM Customer Churn - Data Profiling Report",
        explorative=True,
    )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    profile.to_file(REPORT_PATH)

    print(f"Profiling report created: {REPORT_PATH}")


if __name__ == "__main__":
    main()