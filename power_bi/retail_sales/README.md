# Retail Store Sales Power BI Dashboard

This Power BI dashboard is the final visual reporting layer of the **Retail Store Sales Data Cleaning & SQL Trend Analysis** project.

The dashboard is built on top of the cleaned `retail_store_sales_clean.csv` dataset and extends the previous Python data cleaning and SQL analysis stages with interactive reporting and visual storytelling in Power BI.

## Project goal

The goal of this Power BI report is to analyze retail sales performance across:

- overall sales KPIs,
- time trends,
- categories,
- payment methods,
- products,
- month-over-month changes,
- year-over-year changes,
- year-to-date revenue.

The report is designed as a portfolio-ready analytical dashboard showing how cleaned data can be transformed into business insights.

## Report pages

### 1. Sales Overview

The first page provides a high-level overview of sales performance.

Main elements:

- Total Revenue
- Transaction Count
- Average Transaction Value
- Customer Count
- Revenue per Customer
- Revenue by Category
- Monthly Revenue Trend
- Revenue by Payment Method
- Interactive slicers for Location, Payment Method, and Year
- Tooltips with additional KPI context

This page is designed as an executive-style overview of the dataset.

### 2. Time Analysis

The second page focuses on time-based sales analysis.

Main elements:

- YTD Revenue by Month and Year
- Month-over-Month Revenue Change %
- YoY Revenue Change % by Year-Month
- Tooltip-based context for monthly revenue, previous period revenue, and percentage changes

The report uses a dedicated `DimDate` table connected to the sales table by `transaction_date`.

Time intelligence measures include:

- Previous Month Revenue
- MoM Revenue Change
- MoM Revenue Change %
- YTD Revenue
- Previous Year Revenue
- YoY Revenue Change
- YoY Revenue Change %

Note: 2025 contains only partial data and should not be interpreted as a full-year trend.

### 3. Category Analysis

The third page focuses on category and product-level performance.

Main elements:

- Revenue by Category
- Transaction Count by Category
- Average Transaction Value by Category
- Revenue Share by Category
- Top Items by Revenue
- Category Filter dropdown for product-level exploration
- Tooltips with revenue, transaction count, average transaction value, customer count, and category share

The Category Filter is configured mainly to support the `Top Items by Revenue` visual while keeping the category comparison visuals readable.

### 4. Customer Analysis

The fourth page focuses on customer-level sales performance.

Main elements:
- Top Customers by Revenue
- Top Customers by Transaction Count
- Top Customers by Avg Transaction Value
- Customer Revenue Share %
- Filters for Year, Location, and Payment Method
- Tooltips with revenue, transaction count, average transaction value, and customer share

This page helps identify whether top customers generate revenue mainly through transaction volume or higher average transaction value.

## Data model

The report uses:

- `retail_store_sales_clean` as the main sales table
- `DimDate` as a dedicated date table

Relationship:

- `DimDate[Date]` 1 → * `retail_store_sales_clean[transaction_date]`

The `DimDate` table includes:

- Date
- Year
- Month Number
- Month Name
- Year-Month
- Quarter

`Month Name` is sorted by `Month Number`.

Additional improvements after review:
- Created a dedicated Measures table for DAX measures
- Added data labels to key visuals
- Added conditional colors for positive and negative MoM/YoY changes
- Added additional filters for Time, Category, and Customer analysis pages
- Added Customer Analysis page
- Replaced duplicated category revenue visual with category revenue split by location
- 
## Key DAX measures

### Total Revenue

```DAX
Total Revenue =
SUM(retail_store_sales_clean[total_spent])
```

### Transaction Count

```DAX
Transaction Count =
COUNT(retail_store_sales_clean[transaction_id])
```

### Average Transaction Value

```DAX
Average Transaction Value =
DIVIDE(
    [Total Revenue],
    [Transaction Count]
)
```

### Customer Count

```DAX
Customer Count =
DISTINCTCOUNT(retail_store_sales_clean[customer_id])
```

### Revenue per Customer

```DAX
Revenue per Customer =
DIVIDE(
    [Total Revenue],
    [Customer Count]
)
```

### Previous Month Revenue

```DAX
Previous Month Revenue =
CALCULATE(
    [Total Revenue],
    PREVIOUSMONTH(DimDate[Date])
)
```

### MoM Revenue Change

```DAX
MoM Revenue Change =
[Total Revenue] - [Previous Month Revenue]
```

### MoM Revenue Change %

```DAX
MoM Revenue Change % =
DIVIDE(
    [MoM Revenue Change],
    [Previous Month Revenue]
)
```

### YTD Revenue

```DAX
YTD Revenue =
TOTALYTD(
    [Total Revenue],
    DimDate[Date]
)
```

### Previous Year Revenue

```DAX
Previous Year Revenue =
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(DimDate[Date])
)
```

### YoY Revenue Change

```DAX
YoY Revenue Change =
[Total Revenue] - [Previous Year Revenue]
```

### YoY Revenue Change %

```DAX
YoY Revenue Change % =
DIVIDE(
    [YoY Revenue Change],
    [Previous Year Revenue]
)
```

### Category Revenue Share %

```DAX
Category Revenue Share % =
DIVIDE(
    [Total Revenue],
    CALCULATE(
        [Total Revenue],
        ALL(retail_store_sales_clean[category])
    )
)
```
### Customer Revenue Share %

```DAX
Customer Revenue Share % =
DIVIDE(
    [Total Revenue],
    CALCULATE(
        [Total Revenue],
        ALL(retail_store_sales_clean[customer_id])
    )
)
```

## Tools used

- Power BI Desktop
- Power Query
- DAX
- Python / pandas for the data cleaning stage
- SQL for previous analytical queries
- GitHub for project documentation

## Project context

This dashboard is part of a larger end-to-end retail analytics portfolio project.

Project stages:

1. Python / pandas data cleaning
2. SQL sales analysis
3. Power BI dashboard and visual storytelling

The Power BI dashboard demonstrates how cleaned transactional data can be turned into an interactive analytical report with KPIs, slicers, tooltips, a dedicated date table, and time intelligence measures.
