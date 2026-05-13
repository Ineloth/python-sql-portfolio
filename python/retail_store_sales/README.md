# Retail Store Sales - Python Data Cleaning

This folder contains the Python cleaning script for the **Retail Store Sales Data Cleaning & SQL Trend Analysis** project.
Purpose

The goal of the script is to transform the raw retail sales dataset into a clean analytical CSV file ready for SQL analysis.

# Main cleaning steps

The script performs the following steps:

Loads the raw CSV file.
Checks duplicates and missing values.
Validates the relationship:
Total Spent = Price Per Unit * Quantity
Recovers missing Price Per Unit values using:
Total Spent / Quantity
Recovers missing Item values using a lookup based on:
Category + Price Per Unit
Fills missing Discount Applied values as unknown.
Removes rows where both Quantity and Total Spent are missing.
Parses Transaction Date into a clean date format.
Renames columns to snake_case.
Exports the cleaned CSV file.
Output

# The script exports:

data/retail_store_sales/clean/retail_store_sales_clean.csv
Key results
609 missing unit prices recovered
1,213 missing item names recovered
604 non-recoverable rows excluded from revenue analysis
11,971 final clean rows
