-- Query 13: Monthly payment method share
-- Purpose:
--   Analyze how payment method revenue share changes month by month.
--
-- Dataset:
--   retail_store_sales_clean
--
-- Key SQL concepts:
--   CTE, GROUP BY, SUM() OVER(), DENSE_RANK(), PARTITION BY, NULLIF(), ROUND()

with payment_sales as (select strftime('%Y-%m', r.transaction_date) as sales_month,
r.payment_method,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as payment_total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by strftime('%Y-%m', r.transaction_date),r.payment_method),

month_total_revenue as (select sales_month,
payment_method,
transaction_count,
payment_total_revenue,
avg_transaction_value,
sum(payment_total_revenue) over (partition by sales_month) as monthly_total_revenue
from payment_sales)

select sales_month,
dense_rank() over (partition by sales_month order by payment_total_revenue desc) as payment_monthly_rank,
payment_method,
transaction_count,
round(avg_transaction_value,2) as avg_transaction_value,
round(payment_total_revenue,2) as payment_total_revenue,
round(monthly_total_revenue,2) as monthly_total_revenue,
round((payment_total_revenue*100.0)/nullif(monthly_total_revenue,0),2) as payment_revenue_share
from month_total_revenue
order by sales_month,payment_monthly_rank;
