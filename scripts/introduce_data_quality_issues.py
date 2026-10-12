import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
CORRUPTED_DIR = BASE_DIR / "data" / "corrupted"

CORRUPTED_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# LOAD PRODUCTION DATA
# ============================================================

production_df = pd.read_csv(
    RAW_DIR / "production.csv"
)

print(
    f"Original records: "
    f"{len(production_df):,}"
)


# ============================================================
# REPRODUCIBILITY
# ============================================================

np.random.seed(42)


# ============================================================
# 1. DUPLICATE RECORD
# ============================================================

duplicate_record = production_df.sample(
    n=10,
    random_state=42
)

production_df = pd.concat(
    [
        production_df,
        duplicate_record
    ],
    ignore_index=True
)


# ============================================================
# 2. NULL MACHINE ID
# ============================================================

null_indices = np.random.choice(
    production_df.index,
    size=20,
    replace=False
)

production_df.loc[
    null_indices,
    "machine_id"
] = np.nan


# ============================================================
# 3. INVALID MACHINE ID
# ============================================================

invalid_indices = np.random.choice(
    production_df.index,
    size=10,
    replace=False
)

production_df.loc[
    invalid_indices,
    "machine_id"
] = "M999"


# ============================================================
# 4. NEGATIVE ACTUAL QUANTITY
# ============================================================

negative_indices = np.random.choice(
    production_df.index,
    size=10,
    replace=False
)

production_df.loc[
    negative_indices,
    "actual_quantity"
] = -50


# ============================================================
# 5. INVALID PRODUCTION STATUS
# ============================================================

status_indices = np.random.choice(
    production_df.index,
    size=10,
    replace=False
)

production_df.loc[
    status_indices,
    "production_status"
] = "Unknown"


# ============================================================
# SAVE CORRUPTED DATA
# ============================================================

output_path = (
    CORRUPTED_DIR /
    "production.csv"
)

production_df.to_csv(
    output_path,
    index=False
)


# ============================================================
# SUMMARY
# ============================================================

print(
    f"Corrupted records: "
    f"{len(production_df):,}"
)

print(
    f"Output: {output_path}"
)  



# ============================================================
# LOAD QUALITY INSPECTION DATA
# ============================================================

quality_df = pd.read_csv(
    RAW_DIR / "quality_inspection.csv"
)

print(
    f"\nOriginal quality records: "
    f"{len(quality_df):,}"
)


# ============================================================
# 1. DUPLICATE INSPECTION RECORDS
# ============================================================

duplicate_quality = quality_df.sample(
    n=10,
    random_state=42
)

quality_df = pd.concat(
    [
        quality_df,
        duplicate_quality
    ],
    ignore_index=True
)


# ============================================================
# 2. NULL PRODUCTION ID
# ============================================================

null_indices = np.random.choice(
    quality_df.index,
    size=20,
    replace=False
)

quality_df.loc[
    null_indices,
    "production_id"
] = np.nan


# ============================================================
# 3. INVALID PRODUCTION ID
# ============================================================

invalid_indices = np.random.choice(
    quality_df.index,
    size=10,
    replace=False
)

quality_df.loc[
    invalid_indices,
    "production_id"
] = "PRD999999"


# ============================================================
# 4. DEFECT QUANTITY > INSPECTED QUANTITY
# ============================================================

invalid_quantity_indices = np.random.choice(
    quality_df.index,
    size=10,
    replace=False
)

quality_df.loc[
    invalid_quantity_indices,
    "defect_quantity"
] = (
    quality_df.loc[
        invalid_quantity_indices,
        "inspected_quantity"
    ]
    + 50
)


# ============================================================
# 5. INVALID QUALITY STATUS
# ============================================================

invalid_status_indices = np.random.choice(
    quality_df.index,
    size=10,
    replace=False
)

quality_df.loc[
    invalid_status_indices,
    "quality_status"
] = "Unknown"


# ============================================================
# SAVE CORRUPTED QUALITY DATA
# ============================================================

quality_output_path = (
    CORRUPTED_DIR /
    "quality_inspection.csv"
)

quality_df.to_csv(
    quality_output_path,
    index=False
)


# ============================================================
# SUMMARY
# ============================================================

print(
    f"Corrupted quality records: "
    f"{len(quality_df):,}"
)

print(
    f"Output: {quality_output_path}"
)