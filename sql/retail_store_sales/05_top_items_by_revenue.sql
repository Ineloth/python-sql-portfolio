-- Query 05: Top items by revenue
-- Purpose:
--   Identify the top 10 products by total revenue across the full dataset.
--
-- Dataset:
--   retail_store_sales_clean
--
-- Key SQL concepts:
--   CTE, GROUP BY, DENSE_RANK(), WHERE, ROUND()

with item_sales as (select r.item,
r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as item_revenue,
avg(r.total_spent) as avg_transaction_value,
sum(r.quantity) as item_quantity
from retail_store_sales_clean r
group by item,category),

item_rank as (select item,
category,
transaction_count,
item_revenue,
avg_transaction_value,
item_quantity,
dense_rank() over (order by item_revenue desc) as item_revenue_rank
from item_sales)

select item_revenue_rank,
item,
category,
transaction_count,
round(item_revenue, 2) as item_revenue,
round(avg_transaction_value, 2) as avg_transaction_value,
item_quantity
from item_rank
where item_revenue_rank<=10
order by item_revenue_rank;
