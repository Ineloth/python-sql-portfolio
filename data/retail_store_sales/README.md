# Retail Store Sales Dataset

This folder contains data files used in the **Retail Store Sales Data Cleaning & SQL Trend Analysis** project.

## Folder structure

```text
data/retail_store_sales/
├── raw/
└── clean/

#  Raw data

The raw dataset contains messy retail transaction data with missing values in several columns, including:

Item
Price Per Unit
Quantity
Total Spent
Discount Applied

The raw file is used as the starting point for the Python data cleaning process.

# Clean data

The cleaned dataset is stored in:

clean/retail_store_sales_clean.csv

The clean file was prepared with pandas and is intended for SQL analysis.

# Cleaning summary

Key cleaning results:

Raw rows: 12,575
Clean rows: 11,971
Removed non-recoverable sales rows: 604
Recovered missing Price Per Unit values: 609
Recovered missing Item values: 1,213
Missing Discount Applied values filled as unknown
Final dataset contains no missing values in analytical columns
Notes

Rows missing both Quantity and Total Spent were excluded from the clean dataset because revenue-related values could not be recovered without assumptions.
