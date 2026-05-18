with payment_revenue as (select r.payment_method,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.payment_method),

overall_profits as (select payment_method,
transaction_count,
total_revenue,
sum(total_revenue) over () as overall_revenue,
avg_transaction_value
from payment_revenue)

select dense_rank() over (order by total_revenue desc) as payment_revenue_rank,
payment_method,
transaction_count as transaction_count,
round(total_revenue,2) as total_revenue,
round(overall_revenue,2) as overall_revenue,
round((total_revenue*100.0)/nullif(overall_revenue,0),2) as payment_revenue_share,
round(avg_transaction_value,2) as avg_transaction_value
from overall_profits
order by payment_revenue_rank;