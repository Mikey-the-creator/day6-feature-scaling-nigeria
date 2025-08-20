# Day 6 — Feature Scaling with NumPy & Pandas (Nigeria Dataset)

This mini-project demonstrates **feature scaling** (Min–Max) on a tiny dataset of Nigerian states (Population, Temperature).

## What’s inside
- `data/nigerian_states.csv` — raw sample data you can edit.
- `scripts/matrix_ops.py` — reads CSV, scales selected numeric columns, writes `nigerian_states_scaled.csv`.
- `requirements.txt` — Python dependencies.

## Why scale?
Different features (e.g., Population in millions vs Temperature in °C) have very different ranges. Scaling brings them to a comparable range (0–1), which helps many ML algorithms converge faster and prevents large-range features from dominating.

## How to run (local)
```bash
# 1) Optional: create a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the script
python scripts/matrix_ops.py
