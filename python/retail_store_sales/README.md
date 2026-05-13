# Retail Store Sales - Python Data Cleaning

This folder contains the Python cleaning script for the **Retail Store Sales Data Cleaning & SQL Trend Analysis** project.

## Script

- `retail_store_sales_cleaning.py`

## Purpose

The goal of the script is to transform the raw retail sales dataset into a clean analytical CSV file ready for SQL analysis.

## Main cleaning steps

The script performs the following steps:

1. Loads the raw CSV file.
2. Checks duplicates and missing values.
3. Validates the relationship: `Total Spent = Price Per Unit * Quantity`.
4. Recovers missing `Price Per Unit` values using: `Total Spent / Quantity`.
5. Recovers missing `Item` values using a lookup based on `Category + Price Per Unit`.
6. Fills missing `Discount Applied` values as `unknown`.
7. Removes rows where both `Quantity` and `Total Spent` are missing.
8. Parses `Transaction Date` into a clean date format.
9. Renames columns to `snake_case`.
10. Exports the cleaned CSV file.

## Output

The script exports:

- `data/retail_store_sales/clean/retail_store_sales_clean.csv`

## Key results

- 609 missing unit prices recovered
- 1,213 missing item names recovered
- 604 non-recoverable rows excluded from revenue analysis
- 11,971 final clean rows
