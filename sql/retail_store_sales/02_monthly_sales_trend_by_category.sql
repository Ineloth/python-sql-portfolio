-- Query 02: Monthly sales trend by category
-- Purpose:
--   Analyze monthly revenue trends separately for each product category,
--   including previous category revenue, revenue change and percentage change.
--
-- Dataset:
--   retail_store_sales_clean
--
-- Key SQL concepts:
--   CTE, GROUP BY, LAG(), PARTITION BY, CASE, NULLIF(), ROUND()

with month_sales as (select strftime('%Y-%m',r.transaction_date) as sales_month,
r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by strftime('%Y-%m',r.transaction_date), r.category),

previous_sales as (select sales_month,
category,
transaction_count,
total_revenue,
avg_transaction_value,
lag (total_revenue) over (PARTITION by category order by sales_month) as previous_revenue
from month_sales),

sales_change as (select sales_month,
category,
transaction_count,
avg_transaction_value,
total_revenue,
previous_revenue,
total_revenue-previous_revenue as revenue_change
from previous_sales)

select sales_month,
category,
transaction_count,
round(avg_transaction_value,2) as avg_transaction_value,
round(total_revenue,2) as total_revenue,
round(previous_revenue,2) as previous_revenue,
round(revenue_change,2) as revenue_change,
round((revenue_change*100.0)/nullif(previous_revenue,0),2) as revenue_change_percent,
case 
    when previous_revenue is null then 'first month'
    when revenue_change > 0 then 'increase'
    when revenue_change < 0 then 'decrease'
    else 'no change'
    end as revenue_trend_status
from sales_change
order by category, sales_month;
