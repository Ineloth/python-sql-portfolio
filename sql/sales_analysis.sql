-- Sales Analysis in SQL
-- Mini project based on the same sales dataset used in the Python/pandas project.
-- Goal: practice basic SQL reporting with SELECT, GROUP BY, aggregation and CASE.

SELECT s.city,
round(sum(s.revenue),2) as total_revenue,
round(sum(s.discounted_revenue),2) as total_discounted_rev,
round(sum(s.discount_loss),2) as discount_loss,
case when sum(s.revenue)-sum(s.discounted_revenue)>sum(s.revenue)*0.05 then 'big discount' else 'small discount' end as discount_status
from sales_clean_for_sql s
group by s.city
order by total_revenue desc;
-- Revenue and discount impact by city
-- Cities are classified as "big discount" if discount loss exceeds 5% of total revenue.

