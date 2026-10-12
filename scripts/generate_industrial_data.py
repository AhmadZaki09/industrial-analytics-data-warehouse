import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# MACHINE MASTER DATA
# ============================================================

machines = [
    {
        "machine_id": "M001",
        "machine_name": "CNC Machine 01",
        "machine_type": "CNC",
        "production_line": "LINE-A",
        "plant": "PLANT-01",
        "installation_date": "2022-03-15",
        "status": "Active",
    },
    {
        "machine_id": "M002",
        "machine_name": "Press Machine 01",
        "machine_type": "PRESS",
        "production_line": "LINE-A",
        "plant": "PLANT-01",
        "installation_date": "2021-07-20",
        "status": "Active",
    },
    {
        "machine_id": "M003",
        "machine_name": "Welding Robot 01",
        "machine_type": "ROBOT",
        "production_line": "LINE-B",
        "plant": "PLANT-01",
        "installation_date": "2023-01-10",
        "status": "Active",
    },
    {
        "machine_id": "M004",
        "machine_name": "Assembly Machine 01",
        "machine_type": "ASSEMBLY",
        "production_line": "LINE-C",
        "plant": "PLANT-02",
        "installation_date": "2022-11-05",
        "status": "Maintenance",
    },
    {
        "machine_id": "M005",
        "machine_name": "Packaging Machine 01",
        "machine_type": "PACKAGING",
        "production_line": "LINE-C",
        "plant": "PLANT-02",
        "installation_date": "2024-02-18",
        "status": "Active",
    },
]

machine_df = pd.DataFrame(machines)

machine_df.to_csv(
    RAW_DIR / "machine.csv",
    index=False
)


# ============================================================
# PRODUCT MASTER DATA
# ============================================================

products = [
    {
        "product_id": "P001",
        "product_name": "Industrial Pump A",
        "product_category": "Pump",
        "unit_price": 12500000,
    },
    {
        "product_id": "P002",
        "product_name": "Industrial Pump B",
        "product_category": "Pump",
        "unit_price": 15800000,
    },
    {
        "product_id": "P003",
        "product_name": "Valve Type A",
        "product_category": "Valve",
        "unit_price": 4500000,
    },
    {
        "product_id": "P004",
        "product_name": "Steel Component X",
        "product_category": "Component",
        "unit_price": 2750000,
    },
    {
        "product_id": "P005",
        "product_name": "Industrial Filter A",
        "product_category": "Filter",
        "unit_price": 3200000,
    },
]

product_df = pd.DataFrame(products)

product_df.to_csv(
    RAW_DIR / "product.csv",
    index=False
)



# ============================================================
# PRODUCTION TRANSACTION DATA
# ============================================================

np.random.seed(42)

NUM_PRODUCTION = 50000

production_ids = [
    f"PRD{i:06d}"
    for i in range(1, NUM_PRODUCTION + 1)
]

production_dates = pd.date_range(
    start="2026-01-01",
    end="2026-09-28",
    periods=NUM_PRODUCTION
)

machine_ids = np.random.choice(
    machine_df["machine_id"],
    size=NUM_PRODUCTION
)

product_ids = np.random.choice(
    product_df["product_id"],
    size=NUM_PRODUCTION
)

planned_quantity = np.random.randint(
    300,
    1000,
    size=NUM_PRODUCTION
)

# Actual quantity dibuat sedikit lebih rendah
# daripada planned quantity
actual_quantity = (
    planned_quantity
    - np.random.randint(
        0,
        50,
        size=NUM_PRODUCTION
    )
)

downtime_minutes = np.random.randint(
    0,
    120,
    size=NUM_PRODUCTION
)

production_status = np.random.choice(
    [
        "Completed",
        "Completed",
        "Completed",
        "Delayed",
        "Cancelled"
    ],
    size=NUM_PRODUCTION
)

production_df = pd.DataFrame({
    "production_id": production_ids,
    "production_date": production_dates,
    "machine_id": machine_ids,
    "product_id": product_ids,
    "planned_quantity": planned_quantity,
    "actual_quantity": actual_quantity,
    "downtime_minutes": downtime_minutes,
    "production_status": production_status
})

production_df.to_csv(
    RAW_DIR / "production.csv",
    index=False
)

print("\nProduction dataset:")
print(production_df.head())

print(
    f"\nTotal production records: "
    f"{len(production_df):,}"
)



# ============================================================
# MAINTENANCE TRANSACTION DATA
# ============================================================

NUM_MAINTENANCE = 5000

maintenance_ids = [
    f"MNT{i:06d}"
    for i in range(1, NUM_MAINTENANCE + 1)
]

maintenance_dates = pd.date_range(
    start="2026-01-01",
    end="2026-09-28",
    periods=NUM_MAINTENANCE
)

maintenance_machine_ids = np.random.choice(
    machine_df["machine_id"],
    size=NUM_MAINTENANCE
)

maintenance_types = np.random.choice(
    [
        "Preventive",
        "Corrective",
        "Emergency"
    ],
    size=NUM_MAINTENANCE,
    p=[0.60, 0.30, 0.10]
)

downtime_hours = np.round(
    np.random.uniform(
        0.5,
        12.0,
        size=NUM_MAINTENANCE
    ),
    2
)

maintenance_cost = np.round(
    np.random.uniform(
        500000,
        5000000,
        size=NUM_MAINTENANCE
    ),
    0
)

technicians = np.random.choice(
    [
        "Budi",
        "Andi",
        "Rizky",
        "Dimas",
        "Fajar"
    ],
    size=NUM_MAINTENANCE
)

descriptions = np.random.choice(
    [
        "Routine inspection",
        "Oil replacement",
        "Component replacement",
        "Motor inspection",
        "Sensor calibration",
        "Emergency repair"
    ],
    size=NUM_MAINTENANCE
)

maintenance_df = pd.DataFrame({
    "maintenance_id": maintenance_ids,
    "machine_id": maintenance_machine_ids,
    "maintenance_date": maintenance_dates,
    "maintenance_type": maintenance_types,
    "downtime_hours": downtime_hours,
    "maintenance_cost": maintenance_cost,
    "technician": technicians,
    "description": descriptions
})

maintenance_df.to_csv(
    RAW_DIR / "maintenance.csv",
    index=False
)

print("\nMaintenance dataset:")
print(maintenance_df.head())

print(
    f"\nTotal maintenance records: "
    f"{len(maintenance_df):,}"
)



# ============================================================
# QUALITY INSPECTION DATA
# ============================================================

NUM_INSPECTIONS = 40000

inspection_ids = [
    f"INS{i:06d}"
    for i in range(1, NUM_INSPECTIONS + 1)
]

# Ambil production records secara random
sampled_production = production_df.sample(
    n=NUM_INSPECTIONS,
    random_state=42
).reset_index(drop=True)

inspection_dates = (
    pd.to_datetime(sampled_production["production_date"])
    + pd.to_timedelta(
        np.random.randint(
            1,
            8,
            size=NUM_INSPECTIONS
        ),
        unit="h"
    )
)

inspected_quantity = sampled_production[
    "actual_quantity"
].to_numpy()

defect_quantity = np.minimum(
    np.random.poisson(
        lam=5,
        size=NUM_INSPECTIONS
    ),
    inspected_quantity
)

defect_types = np.where(
    defect_quantity == 0,
    "None",
    np.random.choice(
        [
            "Surface Defect",
            "Dimension Error",
            "Material Defect",
            "Assembly Error"
        ],
        size=NUM_INSPECTIONS
    )
)

quality_status = np.where(
    defect_quantity == 0,
    "Passed",
    np.where(
        defect_quantity / inspected_quantity <= 0.05,
        "Passed",
        "Failed"
    )
)

quality_df = pd.DataFrame({
    "inspection_id": inspection_ids,
    "production_id": sampled_production["production_id"],
    "inspection_date": inspection_dates,
    "machine_id": sampled_production["machine_id"],
    "product_id": sampled_production["product_id"],
    "inspected_quantity": inspected_quantity,
    "defect_quantity": defect_quantity,
    "defect_type": defect_types,
    "quality_status": quality_status
})

quality_df.to_csv(
    RAW_DIR / "quality_inspection.csv",
    index=False
)

print("\nQuality inspection dataset:")
print(quality_df.head())

print(
    f"\nTotal quality inspection records: "
    f"{len(quality_df):,}"
)


# ============================================================
# PREVIEW
# ============================================================

print("Machine dataset:")
print(machine_df)

print("\nProduct dataset:")
print(product_df)

print("\nDataset berhasil dibuat di:")
print(RAW_DIR)