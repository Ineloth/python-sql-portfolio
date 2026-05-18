with overall_kpi as (select count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value,
count(distinct r.customer_id) as customer_count,
count(distinct r.item) as item_count,
count(distinct r.category) as category_count
from retail_store_sales_clean r),

top_category as (select r.category,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.category
order by sum(r.total_spent) desc
limit 1),

top_item as (select r.item,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.item
order by sum(r.total_spent) desc
limit 1),

top_location as (select r.location,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.location
order by sum(r.total_spent) desc
limit 1),

top_payment_method as (select r.payment_method,
count(r.transaction_id) as transaction_count,
sum(r.total_spent) as total_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by r.payment_method
order by sum(r.total_spent) desc
limit 1)

SELECT
o.transaction_count,
round(o.total_revenue, 2) as total_revenue,
round(o.avg_transaction_value, 2) as avg_transaction_value,
o.customer_count,
o.item_count,
o.category_count,

c.category as top_category,
round(c.total_revenue, 2) as top_category_revenue,

i.item as top_item,
round(i.total_revenue, 2) as top_item_revenue,

l.location as top_location,
round(l.total_revenue, 2) as top_location_revenue,

p.payment_method as top_payment_method,
round(p.total_revenue, 2) as top_payment_method_revenue
	
from overall_kpi o
cross join top_category c
cross join top_item i
cross join top_location l
cross join top_payment_method p;
