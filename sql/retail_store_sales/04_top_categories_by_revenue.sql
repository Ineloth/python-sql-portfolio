with category_sales as (select r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as category_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.category),

category_rank as (select category,
transaction_count,
category_revenue,
avg_transaction_value,
dense_rank() over (order by category_revenue desc) as category_revenue_rank
from category_sales)

select category_revenue_rank,
category,
transaction_count,
round(category_revenue,2) as category_revenue,
round(avg_transaction_value,2) as avg_transaction_value
from category_rank
order by category_revenue_rank ;