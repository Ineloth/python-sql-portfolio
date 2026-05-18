-- Query 07: Category rank and share by location
-- Purpose:
--   Analyze category performance within each location, including revenue share
--   and category ranking by location.
--
-- Dataset:
--   retail_store_sales_clean
--
-- Key SQL concepts:
--   CTE, GROUP BY, SUM() OVER(), DENSE_RANK(), PARTITION BY, NULLIF(), ROUND()

with category_revenue as (select r.location,
r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as category_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.location, r.category),

location_revenue as (select location,
category,
transaction_count,
category_revenue,
sum(category_revenue) over (partition by location) as location_total_revenue,
avg_transaction_value
from category_revenue)

select location,
dense_rank() over (partition by location order by category_revenue desc) as category_rank_in_location,
category,
round(avg_transaction_value,2) as avg_category_revenue,
transaction_count,
round(category_revenue,2) as category_revenue,
round(location_total_revenue,2) as location_total_revenue,
round((category_revenue*100.0)/nullif(location_total_revenue,0),2) as category_share_in_location_percent
from location_revenue
order by location,category_rank_in_location;


