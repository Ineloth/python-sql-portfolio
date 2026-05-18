# Retail Store Sales — SQL Analysis

This folder contains SQL queries used to analyze the cleaned retail store sales dataset.

The analysis focuses on:
- monthly and quarterly sales trends,
- revenue changes over time,
- category and item performance,
- location-based sales structure,
- payment method analysis,
- running totals and moving averages,
- executive KPI summary.

## Dataset

The queries use the cleaned table:

`retail_store_sales_clean`

The dataset was prepared in Python and exported as a clean CSV before being imported into SQLite.

## Query list

| File | Analysis |
|---|---|
| 01_monthly_sales_trend.sql | Monthly revenue trend with MoM change |
| 02_monthly_sales_trend_by_category.sql | Monthly trend by category |
| 03_monthly_category_revenue_share.sql | Category revenue share by month |
| 04_top_categories_by_revenue.sql | Top categories by total revenue |
| 05_top_items_by_revenue.sql | Top 10 items by revenue |
| 06_top_items_by_category.sql | Top 3 items within each category |
| 07_category_rank_and_share_by_location.sql | Category rank and share by location |
| 08_monthly_running_total.sql | Monthly cumulative revenue |
| 09_monthly_running_total_by_category.sql | Category-level cumulative revenue |
| 10_moving_average_monthly_revenue.sql | 3-month moving average revenue trend |
| 11_quarterly_sales_trend.sql | Quarterly revenue trend and QoQ change |
| 12_sales_by_payment_method.sql | Revenue analysis by payment method |
| 13_monthly_payment_method_share.sql | Monthly payment method share |
| 14_sales_summary_kpi.sql | One-row executive KPI summary |

## Key SQL techniques

This analysis uses:

- Common Table Expressions,
- aggregation with `GROUP BY`,
- window functions,
- `LAG()` for previous-period comparison,
- `DENSE_RANK()` for ranking,
- running totals with `SUM() OVER()`,
- moving averages with window frames,
- percentage share calculations,
- `CASE` statements,
- `NULLIF()` for safe division,
- `CROSS JOIN` for KPI summary output.

## Business questions answered

The SQL analysis answers questions such as:

- How does revenue change month by month?
- Which categories and items generate the most revenue?
- Which categories dominate in each location?
- How does payment method usage vary over time?
- What is the cumulative revenue trend?
- What are the key sales KPIs for the full dataset?
