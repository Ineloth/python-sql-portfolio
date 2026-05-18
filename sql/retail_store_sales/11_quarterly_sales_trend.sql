with quarter_sales as (select strftime('%Y',r.transaction_date) as year_sales,
count(r.transaction_id) as transaction_count,
case when cast(strftime('%m',r.transaction_date) as INTEGER) BETWEEN 1 and 3 THEN 'Q1'
when cast(strftime('%m',r.transaction_date) as INTEGER) BETWEEN 4 and 6 THEN 'Q2'
when cast(strftime('%m',r.transaction_date) as INTEGER) BETWEEN 7 and 9 THEN 'Q3'
when cast(strftime('%m',r.transaction_date) as INTEGER) BETWEEN 10 and 12 THEN 'Q4'
end as sales_quarter,
sum(r.total_spent) as quarter_revenue,
avg(r.total_spent) as avg_transaction_value
from retail_store_sales_clean r
group by year_sales, sales_quarter),

previous_quarter as (select year_sales,
transaction_count,
sales_quarter,
quarter_revenue,
lag(quarter_revenue) over (order by year_sales,sales_quarter) as previous_quarter_revenue,
avg_transaction_value
from quarter_sales),

change_in_revenue as (select year_sales,
transaction_count,
sales_quarter,
quarter_revenue,
previous_quarter_revenue,
quarter_revenue-previous_quarter_revenue as quarter_change,
avg_transaction_value
from previous_quarter)

select  year_sales,
sales_quarter,
transaction_count,
round(avg_transaction_value,2) as avg_transaction_value,
round(quarter_revenue,2) as quarter_revenue,
round(previous_quarter_revenue,2) as previous_quarter_revenue,
round(quarter_change,2) as quarter_change,
round((quarter_change*100.0)/nullif(previous_quarter_revenue,0),2)  as quarter_change_percent,
case when quarter_change>0 THEN 'revenue increase'
when quarter_change<0 then 'revenue decrease'
when quarter_change is null then 'no data'
else 'equal' end as revenue_change_status
from change_in_revenue
order by year_sales,sales_quarter;
