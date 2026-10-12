# Industrial Analytics Data Warehouse

An end-to-end Data Engineering portfolio project built with Microsoft Fabric to transform manufacturing data into analytics-ready datasets and business insights.

## Project Overview

This project simulates an industrial data platform for analyzing production performance, machine downtime, maintenance activities, and product quality.

It implements a medallion-style architecture from raw CSV ingestion to cleaned Delta tables, an analytical warehouse, and a Power BI dashboard.

## Architecture

```text
CSV Sources
    |
    v
Microsoft Fabric Data Pipelines
    |
    v
Bronze Layer - Raw Data
    |
    v
PySpark Transformation
    |
    v
Silver Layer - Cleaned Delta Tables
    |
    v
Gold Layer - Fabric Warehouse
    |
    v
Semantic Model & Power BI Dashboard
```

## Technology Stack

- Microsoft Fabric
- OneLake and Lakehouse
- Fabric Data Pipelines
- PySpark and Delta Lake
- Fabric Warehouse and T-SQL
- Power BI Semantic Model and DAX

## Data Domains

- Machines
- Products
- Production
- Maintenance
- Quality Inspection

## Engineering Features

- Multi-source CSV ingestion
- Data cleaning and deduplication
- Handling of null, invalid, and inconsistent records
- Delta tables in the Silver layer
- Dimensional modeling in the Gold layer
- Referential integrity validation
- DAX measures for production and quality KPIs
- Interactive manufacturing analytics dashboard

## Dashboard KPIs

- Total Production
- Production Achievement %
- Total Downtime
- Defect Rate %

The dashboard also includes production by machine and production trends over time.

## Data Disclaimer

This project uses synthetic data for learning and portfolio demonstration. It does not represent actual industrial operations.

## Project Status

The initial pipeline, warehouse, semantic model, and first dashboard version have been implemented. Repository documentation and final validation are in progress.