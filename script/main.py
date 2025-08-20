import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Resolve paths relative to this file (main.py is inside "script/", data is at project_root/data/)
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_PATH = DATA_DIR / "nigerian_states.csv"
OUT_PATH = DATA_DIR / "nigerian_states_scaled.csv"
PLOT_PATH = DATA_DIR / "population_temperature_bar.png"

# Actual column names in the CSV
POP_COL = "Population_Estimate_2022"
TEMP_COL = "Average_Temperature_Celsius"

def min_max_scale(col: pd.Series) -> pd.Series:
    mn, mx = col.min(), col.max()
    if mx == mn:
        return pd.Series([0.0] * len(col), index=col.index)
    return (col - mn) / (mx - mn)

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Expected CSV at: {DATA_PATH}. Please verify the path or move the file.")

    df = pd.read_csv(DATA_PATH)

    # Create scaled versions of the real columns
    for c in [POP_COL, TEMP_COL]:
        df[f"Scaled_{c}"] = min_max_scale(pd.to_numeric(df[c], errors="coerce"))

    # Save outputs alongside the input CSV
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved scaled data → {OUT_PATH}")

    x = np.arange(len(df["State"]))  # state positions
    width = 0.35  # bar width

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(x - width/2, df[POP_COL], width, label="Population (raw)", color="steelblue")
    ax1.bar(x + width/2, df[TEMP_COL], width, label="Temperature (°C)", color="salmon")

    ax1.set_xticks(x)
    ax1.set_xticklabels(df["State"], rotation=45, ha="right")
    ax1.set_ylabel("Value")
    ax1.set_title("Population vs Temperature by Nigerian State")
    ax1.legend()

    plt.tight_layout()
    plt.savefig(PLOT_PATH)
    print(f"Saved plot → {PLOT_PATH}")
    plt.show()

if __name__ == "__main__":
    main()
