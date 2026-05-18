with monthly_sales as (select strftime ('%Y-%m', r.transaction_date) as sales_month,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as monthly_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by strftime ('%Y-%m', r.transaction_date)),

moving_average as (select sales_month,
transaction_count,
monthly_revenue,
avg_transaction_value,
avg(monthly_revenue) over (order by sales_month
rows between 2 PRECEDING and CURRENT row) as moving_3_month_average
from monthly_sales)

select sales_month,
transaction_count,
round(monthly_revenue,2) as monthly_revenue,
round(moving_3_month_average,2) as moving_avg_3_month_revenue,
round(avg_transaction_value,2) as avg_transaction_value
from moving_average
order by sales_month;