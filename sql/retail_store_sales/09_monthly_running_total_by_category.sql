-- Query 09: Monthly running total by category
-- Purpose:
--   Calculate cumulative monthly revenue separately for each category.
--
-- Dataset:
--   retail_store_sales_clean
--
-- Key SQL concepts:
--   CTE, GROUP BY, SUM() OVER(), PARTITION BY, ORDER BY, ROUND()

with monthly_sales as (select strftime('%Y-%m', r.transaction_date) as sales_month,
r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as monthly_revenue,
avg(r.total_spent) as avg_monthly_revenue
from retail_store_sales_clean r
group by strftime('%Y-%m', r.transaction_date),r.category),

cat_running_revenue as (select sales_month,
category,
transaction_count,
monthly_revenue,
avg_monthly_revenue,
sum(monthly_revenue) over (partition by category order by sales_month) as category_total_running_revenue
from monthly_sales)

select sales_month,
category,
transaction_count,
round(monthly_revenue,2) as monthly_revenue,
round(avg_monthly_revenue,2) as avg_monthly_revenue,
round(category_total_running_revenue,2) as category_total_running_revenue
from cat_running_revenue
order by category,sales_month;
