## How to use

1. Download `sales_clean_for_sql.csv`.
2. Import it into SQLite as table `sales_clean_for_sql`.
3. Run queries from `sales_analysis.sql`.


This analysis measures the share of laptop revenue in total revenue for each sales channel.
The results suggest that the digital channel is the most dependent on laptop sales, while other channels show little or no visible laptop revenue contribution.
The query combines intermediate reports with CTEs and a LEFT JOIN to compare total channel revenue against laptop-specific revenue.

This analysis focuses on Q1 sales by city and compares total quantity sold with total revenue generated.
The results show that high sales volume does not always translate into equally high revenue, which may suggest differences in average transaction value between cities.
Simple volume and revenue labels were added to make the comparison easier to read.
