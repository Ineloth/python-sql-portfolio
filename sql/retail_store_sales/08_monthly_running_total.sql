with monthly_sales as (select strftime('%Y-%m', r.transaction_date) as sales_month,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as monthly_revenue,
avg(r.total_spent) as avg_monthly_revenue
from retail_store_sales_clean r
group by strftime('%Y-%m', r.transaction_date)),

running_revenue as (select sales_month,
transaction_count,
monthly_revenue,
avg_monthly_revenue,
sum(monthly_revenue) over (order by sales_month) as running_total_revenue
from monthly_sales)

select sales_month,
transaction_count,
round(monthly_revenue,2) as monthly_revenue,
round(avg_monthly_revenue,2) as avg_monthly_revenue,
round(running_total_revenue,2) as running_total_revenue
from running_revenue
order by sales_month;