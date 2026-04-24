# Date Cleaning & Sales Analysis Project

This is a mini project focused on:
- cleaning messy date formats using pandas
- validating data quality
- analyzing sales data after cleaning

## What was done

- handled multiple date formats (DD/MM/YYYY, YYYY-MM-DD, etc.)
- identified ambiguous and invalid dates
- created data quality flags:
  - safe_to_parse
  - invalid_date
  - unrecognized_format
  - empty_date
- separated date and time into different columns

## Data analysis

After cleaning the data:
- revenue analysis by city and channel
- product performance analysis
- discount impact analysis

## Key findings

- Krakow generated the highest revenue, followed by Warsaw
- Electronics products drive most of the revenue
- Different sales patterns observed between cities and channels
- Discounts had the biggest impact on Mouse sales

## Example outputs

### Data quality summary
![Data Quality](./summary_df.png)

### Discount impact analysis
![Discount Analysis](./discount_impact_summary.png)
