-- Query 03: Monthly category revenue share
-- Purpose:
--   Calculate each category's revenue share within every month.
--
-- Dataset:
--   retail_store_sales_clean
--
-- Key SQL concepts:
--   CTE, GROUP BY, SUM() OVER(), PARTITION BY, NULLIF(), ROUND()

with category_monthly_sales  as (select strftime('%Y-%m',r.transaction_date) as sales_month,
r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as category_revenue
from retail_store_sales_clean r
group by strftime('%Y-%m',r.transaction_date), r.category),

monthly_revenue as (select sales_month,
category,
transaction_count,
category_revenue,
sum(category_revenue) over (partition by sales_month) as monthly_total_revenue
from category_monthly_sales )

select sales_month,
category,
transaction_count,
round(category_revenue,2) as category_revenue,
round(monthly_total_revenue,2) as monthly_total_revenue,
round((category_revenue * 100.0)/nullif(monthly_total_revenue,0),2) as category_revenue_share_percent
from monthly_revenue
order by sales_month, category_revenue_share_percent DESC;
