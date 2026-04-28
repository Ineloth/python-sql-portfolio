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

--||----||----||----||----||----||----||----||----||----||----||----||----||----||----||--

Select s.product,
s.channel_group,
sum(s.qty) as total_qty,
sum(s.revenue) as total_revenue,
sum(s.discount_loss) as discount_loss,
sum(s.discounted_revenue) as total_discount_rev,
round((cast(sum(s.discount_loss)as real)/nullif(sum(s.revenue),0)),2) as discount_ratio,
case when sum(s.qty)>3 and round((cast(sum(s.discount_loss)as real)/nullif(sum(s.revenue),0)),2)>=0.05
then 'high discount impact' else 'low discount impact' end as discount_impact_status
from sales_clean_for_sql s
group by s.product, s.channel_group
Order by s.product asc;

--Discounts seem to have a stronger impact in store sales channels than in digital ones, 
--as high-volume and higher-discount combinations appear more frequently in store-based sales.

--||----||----||----||----||----||----||----||----||----||----||----||----||----||----||--

with sub_channel as (select s.channel_group,
sum(s.revenue) as total_revenue
from sales_clean_for_sql s
group by channel_group),

sub_laptop as (select s.channel_group,
sum(s.revenue) as total_revenue
FROM sales_clean_for_sql s
where s.product = 'Laptop'
group by s.channel_group)

select sub_channel.channel_group,
sub_channel.total_revenue,
coalesce(sub_laptop.total_revenue, 0.0) as total_laptop_revenue,
coalesce(round(cast(coalesce(sub_laptop.total_revenue, 0.0) as real)/nullif(sub_channel.total_revenue,0),2), 0.0) as laptop_revenue_share,
case 
when round(cast(coalesce(sub_laptop.total_revenue, 0.0) as real)/nullif(sub_channel.total_revenue,0),2) > 0.5 then 'high laptop dependency'
when round(cast(coalesce(sub_laptop.total_revenue, 0.0) as real)/nullif(sub_channel.total_revenue,0),2) <=0.5 and round(cast(coalesce(sub_laptop.total_revenue, 0.0) as real)/nullif(sub_channel.total_revenue,0),2) >0.2 then 'medium laptop dependency' 
else 'low laptop dependency' 
end as share_status 

from sub_channel left join sub_laptop on sub_channel.channel_group=sub_laptop.channel_group
order by sub_channel.total_revenue desc;

-- The results suggest that the digital channel is strongly dependent on laptop revenue, 
-- while other channels show little or no visible laptop sales activity.

--||----||----||----||----||----||----||----||----||----||----||----||----||----||----||--

-- Q1 sales performance by city
-- Cities are classified into volume and revenue levels based on Q1 totals in the available dataset.

select s.city,
sum(s.qty) as total_qty,
sum(s.revenue) as total_revenue,
case when sum(s.qty)>= 5 then 'high volume' when sum(s.qty)<3 then 'low volume' else 'medium volume' end as quantity_levels,
case when sum(s.revenue)>= 6000 then 'high revenue' when sum(s.revenue)<3000 then 'low revenue' else 'medium revenue' end as revenue_levels,
'Q1' as quarter
from sales_clean_for_sql s
where s.date_clean >= '2026-01-01' and s.date_clean <'2026-04-01' 
group by s.city
order by total_revenue desc;

-- In Q1, Warsaw showed both high sales volume and high revenue, making it the strongest-performing city in the available dataset.
-- Krakow also performed well in volume, but with lower revenue than Warsaw.
-- Gdansk achieved high volume with relatively low revenue, which may suggest lower average transaction value compared to other cities.
