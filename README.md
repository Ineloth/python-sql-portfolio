# python-sql-portfolio
My first mini project repository for learning Python, SQL and GitHub.

# First Mini Project

This repository is my starting point for learning GitHub and building a small portfolio.

## Goal
I want to keep here my first small Python and SQL projects.

## Planned content
- small Python scripts
- small SQL exercises and mini projects
- simple notes and summaries

## Status
Portfolio in progress.  
Current focus: Python data cleaning, SQL analysis and small end-to-end data projects.

## Projects

### 1. Date Cleaning & Sales Analysis
Mini project focused on data cleaning and basic sales analysis using pandas.

📂 [View project](./python)

### 2. Retail Store Sales Data Cleaning & SQL Trend Analysis

Project focused on cleaning messy retail transaction data with pandas and preparing a clean dataset for SQL trend analysis.

Current stage:
- Python data cleaning completed
- Clean CSV exported
- SQL analysis
- Planned Power BI dashboard

Key cleaning results:
- Raw rows: 12,575
- Clean rows: 11,971
- Recovered missing unit prices: 609
- Recovered missing item names: 1,213
- Removed non-recoverable sales rows: 604
- Missing discount values filled as `unknown`
  
Skills demonstrated:
- pandas data cleaning
- missing value recovery
- lookup-based imputation
- data quality flags
- clean CSV export for SQL analysis

[View Python cleaning script](python/retail_store_sales/retail_store_sales_cleaning.py)

### Retail Store Sales Data Cleaning & SQL Trend Analysis

End-to-end analytical project based on retail sales data.

Current scope:
- data cleaning and validation in Python/pandas,
- missing value recovery using lookup-based logic,
- cleaned CSV export,
- SQL analysis in SQLite,
- monthly and quarterly sales trends,
- category, item, location and payment method analysis,
- window functions, rankings, running totals and moving averages,
- executive KPI summary.

## Power BI dashboard

A Power BI dashboard was added as the final reporting layer of this project.

The dashboard includes:
- Sales Overview
- Time Analysis
- Category Analysis

The report uses a dedicated date table, interactive slicers, tooltips, and DAX time intelligence measures.

