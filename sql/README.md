## How to use

1. Download `sales_clean_for_sql.csv`.
2. Import it into SQLite as table `sales_clean_for_sql`.
3. Run queries from `sales_analysis.sql`.


This analysis measures the share of laptop revenue in total revenue for each sales channel.
The results suggest that the digital channel is the most dependent on laptop sales, while other channels show little or no visible laptop revenue contribution.
The query combines intermediate reports with CTEs and a LEFT JOIN to compare total channel revenue against laptop-specific revenue.
