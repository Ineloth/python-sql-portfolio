import pandas as pd

# Retail Store Sales - Data Cleaning
# This script cleans the raw retail sales dataset and exports a cleaned CSV file for SQL analysis.

# -----------------------------------------------------------------------------
# 1. Load raw dataset
# -----------------------------------------------------------------------------

INPUT_FILE = "data/retail_store_sales/raw/retail_store_sales.csv"
OUTPUT_FILE = "data/retail_store_sales/clean/retail_store_sales_clean.csv"

retail_store_sales = pd.read_csv(INPUT_FILE)

print("Initial preview:")
print(retail_store_sales.head(1))
print("\nInitial missing values:")
print(retail_store_sales.isna().sum())
print("\nRaw rows:", len(retail_store_sales))


# -----------------------------------------------------------------------------
# 2. Initial duplicate checks
# -----------------------------------------------------------------------------

# Full row duplicates were checked during exploration. Transaction ID is the
# business identifier of each transaction, so duplicated Transaction IDs are also
# checked separately.
transaction_id_duplicates = retail_store_sales["Transaction ID"].duplicated(keep="first")
print("\nDuplicated Transaction IDs:", transaction_id_duplicates.sum())


# -----------------------------------------------------------------------------
# 3. Analyze missing sales-related values
# -----------------------------------------------------------------------------

# These masks describe combinations of missing values in the main sales columns.
price_and_quantity = (
    retail_store_sales["Price Per Unit"].isna()
    & retail_store_sales["Quantity"].isna()
)

price_and_spent = (
    retail_store_sales["Price Per Unit"].isna()
    & retail_store_sales["Total Spent"].isna()
)

quantity_and_spent = (
    retail_store_sales["Quantity"].isna()
    & retail_store_sales["Total Spent"].isna()
)

price_quantity_spent = (
    retail_store_sales["Price Per Unit"].isna()
    & retail_store_sales["Quantity"].isna()
    & retail_store_sales["Total Spent"].isna()
)

print("\nMissing sales-value combinations:")
print("Price + Quantity missing:", price_and_quantity.sum())
print("Price + Total Spent missing:", price_and_spent.sum())
print("Quantity + Total Spent missing:", quantity_and_spent.sum())
print("Price + Quantity + Total Spent missing:", price_quantity_spent.sum())


# -----------------------------------------------------------------------------
# 4. Validate Total Spent calculation and Discount Applied behavior
# -----------------------------------------------------------------------------

# Only rows with all three numeric sales columns available are used for this
# consistency check.
all_price_data = (
    retail_store_sales["Price Per Unit"].notna()
    & retail_store_sales["Quantity"].notna()
    & retail_store_sales["Total Spent"].notna()
)

retail_store_sales_data_checks = retail_store_sales.copy()
retail_store_sales_data_checks["expected_total_spent"] = pd.NA
retail_store_sales_data_checks["total_spent_difference"] = pd.NA

retail_store_sales_data_checks.loc[all_price_data, "expected_total_spent"] = (
    retail_store_sales_data_checks.loc[all_price_data, "Quantity"]
    * retail_store_sales_data_checks.loc[all_price_data, "Price Per Unit"]
)

retail_store_sales_data_checks.loc[all_price_data, "total_spent_difference"] = (
    retail_store_sales_data_checks.loc[all_price_data, "Total Spent"]
    - retail_store_sales_data_checks.loc[all_price_data, "expected_total_spent"]
)

non_zero_total_difference = (
    retail_store_sales_data_checks.loc[all_price_data, "total_spent_difference"] != 0
)

print("\nRows with non-zero Total Spent difference among complete numeric rows:", non_zero_total_difference.sum())

# Project conclusion from the validation step:
# Total Spent matches Price Per Unit * Quantity for complete records.
# Discount Applied does not appear to change Total Spent, so missing discount
# values will be treated as an unknown category rather than imputed as True/False.


# -----------------------------------------------------------------------------
# 5. Recover missing Price Per Unit values
# -----------------------------------------------------------------------------

retail_store_sales_data_checks["sales_data_status"] = pd.NA

recovering_price = (
    retail_store_sales_data_checks["Price Per Unit"].isna()
    & retail_store_sales_data_checks["Quantity"].notna()
    & retail_store_sales_data_checks["Total Spent"].notna()
    & (retail_store_sales_data_checks["Quantity"] != 0)
)

print("\nMissing Price Per Unit before recovery:", retail_store_sales_data_checks["Price Per Unit"].isna().sum())
print("Recoverable Price Per Unit rows:", recovering_price.sum())

retail_store_sales_data_checks.loc[recovering_price, "sales_data_status"] = "recovered_price"

retail_store_sales_data_checks.loc[recovering_price, "Price Per Unit"] = (
    retail_store_sales_data_checks.loc[recovering_price, "Total Spent"]
    / retail_store_sales_data_checks.loc[recovering_price, "Quantity"]
)

print("Missing Price Per Unit after recovery:", retail_store_sales_data_checks["Price Per Unit"].isna().sum())


# -----------------------------------------------------------------------------
# 6. Check whether Quantity or Total Spent can be recovered
# -----------------------------------------------------------------------------

recovering_quantity = (
    retail_store_sales_data_checks["Price Per Unit"].notna()
    & retail_store_sales_data_checks["Total Spent"].notna()
    & retail_store_sales_data_checks["Quantity"].isna()
    & (retail_store_sales_data_checks["Price Per Unit"] != 0)
)

recovering_total_spent = (
    retail_store_sales_data_checks["Price Per Unit"].notna()
    & retail_store_sales_data_checks["Total Spent"].isna()
    & retail_store_sales_data_checks["Quantity"].notna()
)

print("\nRecoverable Quantity rows:", recovering_quantity.sum())
print("Recoverable Total Spent rows:", recovering_total_spent.sum())

# Quantity and Total Spent are missing together in 604 rows. These rows cannot be
# recovered without assumptions and will be excluded from the final SQL analysis table.
quantity_and_spent_current = (
    retail_store_sales_data_checks["Quantity"].isna()
    & retail_store_sales_data_checks["Total Spent"].isna()
)

retail_store_sales_data_checks.loc[
    quantity_and_spent_current,
    "sales_data_status"
] = "not_recoverable_missing_quantity_and_total"

complete_sales_status = (
    retail_store_sales_data_checks["Price Per Unit"].notna()
    & retail_store_sales_data_checks["Quantity"].notna()
    & retail_store_sales_data_checks["Total Spent"].notna()
    & retail_store_sales_data_checks["sales_data_status"].isna()
)

retail_store_sales_data_checks.loc[
    complete_sales_status,
    "sales_data_status"
] = "complete_sales_data"

print("Sales data status summary:")
print(retail_store_sales_data_checks["sales_data_status"].value_counts(dropna=False))


# -----------------------------------------------------------------------------
# 7. Recover missing Item values using Category + Price Per Unit lookup
# -----------------------------------------------------------------------------

print("\nMissing Item values before recovery:", retail_store_sales_data_checks["Item"].isna().sum())

recoverable_item_and_price = (
    retail_store_sales_data_checks["Item"].isna()
    & retail_store_sales_data_checks["Price Per Unit"].notna()
)

print("Rows with missing Item and available Price Per Unit:", recoverable_item_and_price.sum())

# Check whether Category + Price Per Unit uniquely identifies Item in complete rows.
existing_item_check = (
    retail_store_sales_data_checks
    .dropna(subset=["Item", "Price Per Unit"])
    .groupby(["Category", "Price Per Unit"])["Item"]
    .nunique()
)

print("Unique Item count per Category + Price Per Unit pair:")
print(existing_item_check.value_counts())

# Build lookup table from complete records.
item_lookup = (
    retail_store_sales_data_checks
    .dropna(subset=["Item", "Price Per Unit"])
    .drop_duplicates(subset=["Category", "Price Per Unit"])
    [["Category", "Price Per Unit", "Item"]]
)

print("Item lookup rules:", len(item_lookup))

# Merge lookup into the working dataframe to create Item_recovered.
retail_store_sales_data_item_check = retail_store_sales_data_checks.merge(
    item_lookup.rename(columns={"Item": "Item_recovered"}),
    on=["Category", "Price Per Unit"],
    how="left"
)

recoverable_item = (
    retail_store_sales_data_item_check["Item"].isna()
    & retail_store_sales_data_item_check["Item_recovered"].notna()
)

print("Recoverable Item rows:", recoverable_item.sum())

# Apply recovered Item values.
retail_store_sales_data_checks = retail_store_sales_data_item_check.copy()

retail_store_sales_data_checks.loc[recoverable_item, "Item"] = (
    retail_store_sales_data_checks.loc[recoverable_item, "Item_recovered"]
)

retail_store_sales_data_checks.loc[
    recoverable_item,
    "item_data_status"
] = "recovered_from_category_and_price"

retail_store_sales_data_checks = retail_store_sales_data_checks.drop(columns=["Item_recovered"])

retail_store_sales_data_checks.loc[
    retail_store_sales_data_checks["item_data_status"].isna(),
    "item_data_status"
] = "item_data_complete"

print("Missing Item values after recovery:", retail_store_sales_data_checks["Item"].isna().sum())
print("Item data status summary:")
print(retail_store_sales_data_checks["item_data_status"].value_counts(dropna=False))


# -----------------------------------------------------------------------------
# 8. Handle missing Discount Applied values
# -----------------------------------------------------------------------------

retail_store_sales_empty_discount = retail_store_sales_data_checks["Discount Applied"].isna()
retail_store_sales_data_checks.loc[
    retail_store_sales_empty_discount,
    "Discount Applied"
] = "unknown"

print("\nDiscount Applied summary after filling missing values:")
print(retail_store_sales_data_checks["Discount Applied"].value_counts(dropna=False))


# -----------------------------------------------------------------------------
# 9. Remove non-recoverable sales rows
# -----------------------------------------------------------------------------

quantity_and_spent_current = (
    retail_store_sales_data_checks["Quantity"].isna()
    & retail_store_sales_data_checks["Total Spent"].isna()
)

print("\nRows before removing non-recoverable sales records:", len(retail_store_sales_data_checks))

retail_store_sales_no_missings = (
    retail_store_sales_data_checks
    .loc[~quantity_and_spent_current]
    .reset_index(drop=True)
    .copy()
)

print("Rows after removing non-recoverable sales records:", len(retail_store_sales_no_missings))


# -----------------------------------------------------------------------------
# 10. Parse Transaction Date
# -----------------------------------------------------------------------------

# Remove leading/trailing whitespace before parsing.
retail_store_sales_no_missings["Transaction Date"] = (
    retail_store_sales_no_missings["Transaction Date"].str.strip()
)

retail_store_sales_no_missings["Transaction Date"] = pd.to_datetime(
    retail_store_sales_no_missings["Transaction Date"],
    format="%Y-%m-%d",
    errors="coerce"
)

print("\nInvalid dates after parsing:", retail_store_sales_no_missings["Transaction Date"].isna().sum())
print("Transaction Date dtype:", retail_store_sales_no_missings["Transaction Date"].dtype)


# -----------------------------------------------------------------------------
# 11. Rename columns and select final structure
# -----------------------------------------------------------------------------

retail_store_sales_clean = retail_store_sales_no_missings.rename(columns={
    "Transaction ID": "transaction_id",
    "Customer ID": "customer_id",
    "Category": "category",
    "Item": "item",
    "Price Per Unit": "price_per_unit",
    "Quantity": "quantity",
    "Total Spent": "total_spent",
    "Payment Method": "payment_method",
    "Location": "location",
    "Transaction Date": "transaction_date",
    "Discount Applied": "discount_applied"
})

final_columns = [
    "transaction_id",
    "customer_id",
    "category",
    "item",
    "price_per_unit",
    "quantity",
    "total_spent",
    "payment_method",
    "location",
    "transaction_date",
    "discount_applied",
    "sales_data_status",
    "item_data_status"
]

retail_store_sales_clean = retail_store_sales_clean[final_columns]
retail_store_sales_clean = retail_store_sales_clean.reset_index(drop=True)


# -----------------------------------------------------------------------------
# 12. Final quality check and export
# -----------------------------------------------------------------------------

print("\nFinal dataset info:")
print(retail_store_sales_clean.info())

print("\nFinal missing values:")
print(retail_store_sales_clean.isna().sum())

print("\nFinal rows:", len(retail_store_sales_clean))

retail_store_sales_clean.to_csv(OUTPUT_FILE, index=False)
print("\nClean dataset exported to:", OUTPUT_FILE)
