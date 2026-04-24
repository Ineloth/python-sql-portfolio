import pandas as pd
import numpy as np

sales_df_big = pd.DataFrame([
    {"order_id": 1001, "product": "Laptop",   "category": "Electronics", "city": "Warsaw", "channel": "Online", "channel_group": "Digital", "price": 4200, "qty": 1, "discount_price": np.nan},
    {"order_id": 1002, "product": "Mouse",    "category": "Accessories", "city": "Krakow", "channel": "Store",  "channel_group": "Offline", "price": 120,  "qty": 2, "discount_price": 99},
    {"order_id": 1003, "product": "Keyboard", "category": "Accessories", "city": "Gdansk", "channel": "Online", "channel_group": np.nan,    "price": 250,  "qty": 1, "discount_price": np.nan},
    {"order_id": 1004, "product": "Monitor",  "category": "Electronics", "city": "Warsaw", "channel": "Store",  "channel_group": "Offline", "price": 1300, "qty": 2, "discount_price": 1199},
    {"order_id": 1005, "product": "Chair",    "category": "Furniture",   "city": "Poznan", "channel": "Online", "channel_group": "Digital", "price": np.nan, "qty": 1, "discount_price": np.nan},
    {"order_id": 1006, "product": "Desk",     "category": "Furniture",   "city": "Wroclaw","channel": "Store",  "channel_group": np.nan,    "price": 900,  "qty": 1, "discount_price": 850},
    {"order_id": 1007, "product": "Laptop",   "category": "Electronics", "city": "Krakow", "channel": "Online", "channel_group": "Digital", "price": 4300, "qty": 1, "discount_price": 3999},
    {"order_id": 1008, "product": "Mouse",    "category": np.nan,        "city": "Gdansk", "channel": "Store",  "channel_group": "Offline", "price": 110,  "qty": 3, "discount_price": np.nan},
    {"order_id": 1009, "product": "Keyboard", "category": "Accessories", "city": "Warsaw", "channel": "Online", "channel_group": "Digital", "price": np.nan, "qty": 2, "discount_price": np.nan},
    {"order_id": 1010, "product": "Monitor",  "category": "Electronics", "city": "Krakow", "channel": "Store",  "channel_group": "Offline", "price": 1250, "qty": np.nan, "discount_price": 1150},

    {"order_id": 1011, "product": "Desk",     "category": "Furniture",   "city": "Gdansk", "channel": "Online", "channel_group": "Digital", "price": 950,  "qty": 1, "discount_price": np.nan},
    {"order_id": 1012, "product": "Chair",    "category": "Furniture",   "city": "Warsaw", "channel": "Store",  "channel_group": "Offline", "price": 600,  "qty": 2, "discount_price": 550},
    {"order_id": 1013, "product": "Laptop",   "category": "Electronics", "city": "Poznan", "channel": "Online", "channel_group": "Digital", "price": 4100, "qty": 1, "discount_price": np.nan},
    {"order_id": 1014, "product": "Mouse",    "category": "Accessories", "city": "Warsaw", "channel": "Store",  "channel_group": "Offline", "price": 115,  "qty": 4, "discount_price": 100},
    {"order_id": 1015, "product": "Keyboard", "category": np.nan,        "city": "Krakow", "channel": "Online", "channel_group": "Digital", "price": 270,  "qty": 2, "discount_price": np.nan},
    {"order_id": 1016, "product": "Monitor",  "category": "Electronics", "city": "Wroclaw","channel": "Store",  "channel_group": "Offline", "price": 1400, "qty": 1, "discount_price": 1299},
    {"order_id": 1017, "product": "Chair",    "category": "Furniture",   "city": "Gdansk", "channel": "Online", "channel_group": "Digital", "price": 650,  "qty": 1, "discount_price": np.nan},
    {"order_id": 1018, "product": "Desk",     "category": "Furniture",   "city": "Warsaw", "channel": "Store",  "channel_group": np.nan,    "price": 980,  "qty": 1, "discount_price": 930},
    {"order_id": 1019, "product": "Laptop",   "category": "Electronics", "city": "Krakow", "channel": "Online", "channel_group": "Digital", "price": 4400, "qty": 1, "discount_price": 4200},
    {"order_id": 1020, "product": "Mouse",    "category": "Accessories", "city": "Poznan", "channel": "Store",  "channel_group": "Offline", "price": np.nan, "qty": 5, "discount_price": np.nan},

    {"order_id": 1003, "product": "Keyboard", "category": "Accessories", "city": "Gdansk", "channel": "Online", "channel_group": np.nan,    "price": 250,  "qty": 1, "discount_price": np.nan},  # full duplicate
    {"order_id": 1007, "product": "Laptop",   "category": "Electronics", "city": "Krakow", "channel": "Online", "channel_group": "Digital", "price": 4350, "qty": 1, "discount_price": 3999},  # near duplicate
    {"order_id": 1010, "product": "Monitor",  "category": "Electronics", "city": "Krakow", "channel": "Store",  "channel_group": "Offline", "price": 1250, "qty": 1, "discount_price": 1150},     # near duplicate
    {"order_id": 1015, "product": "Keyboard", "category": "Accessories", "city": "Krakow", "channel": "Online", "channel_group": "Digital", "price": 270,  "qty": 2, "discount_price": np.nan},      # partially corrected duplicate
    {"order_id": 1021, "product": "Monitor",  "category": "Electronics", "city": "Warsaw", "channel": "Online", "channel_group": "other",   "price": 1500, "qty": 1, "discount_price": np.nan},      # inconsistent text value
    {"order_id": 1022, "product": "Desk",     "category": "Furniture",   "city": "Gdansk", "channel": "Store",  "channel_group": "Other",   "price": 970,  "qty": 1, "discount_price": np.nan},      # inconsistent text value
    {"order_id": 1023, "product": "Chair",    "category": np.nan,        "city": "Poznan", "channel": "Online", "channel_group": "Digital", "price": 620,  "qty": np.nan, "discount_price": np.nan},
    {"order_id": 1024, "product": "Laptop",   "category": "Electronics", "city": "Warsaw", "channel": "Store",  "channel_group": "Offline", "price": 4250, "qty": 1, "discount_price": 4000},
    {"order_id": 1024, "product": "Laptop",   "category": "Electronics", "city": "Warsaw", "channel": "Store",  "channel_group": "Offline", "price": 4250, "qty": 1, "discount_price": 4000},         # full duplicate
    {"order_id": 1025, "product": "Mouse",    "category": "Accessories", "city": "Wroclaw","channel": "Online", "channel_group": np.nan,    "price": 130,  "qty": 2, "discount_price": 120}
])

# This project was built iteratively as a learning exercise.
# The final version keeps the real cleaning logic but removes most of the experimental noise.

# Remove exact duplicates from the raw dataset.
sales_df_big_clean = sales_df_big.drop_duplicates()

# Fill missing values only in columns where replacement is acceptable from a business perspective.
# - channel_group: missing value can be treated as "Unknown"
# - discount_price: missing value can be treated as 0
# Missing values in price, qty, or category are not safely recoverable, so they are not filled here.
sales_df_big_clean = sales_df_big_clean.fillna({"channel_group": "Unknown", "discount_price": 0})

# Keep only records with valid price and qty for revenue analysis.
# Rows with missing price or qty are excluded from the reporting part of the project.
sales_df_big_clean = sales_df_big_clean[~sales_df_big_clean[["qty", "price"]].isna().any(axis=1)].copy()
sales_df_big_clean["revenue"] = sales_df_big_clean["qty"] * sales_df_big_clean["price"]

# Standardize text values in channel_group.
sales_df_big_clean["channel_group"] = sales_df_big_clean["channel_group"].replace({"other": "Other"})

# Add a dirty date column with mixed formats for date-cleaning practice.
dirty_dates = [
    "2026-04-11",
    "11/04/2026",
    "04/11/2026",
    "2026/03/15",
    "15-03-2026",
    "03-15-2026",
    "2026.02.28",
    "28.02.2026",
    "2026-01-05 14:30:00",
    "05/01/2026 08:45",
    "01/05/2026 18:20",
    "2026-13-01",
    "31/02/2026",
    "not a date",
    None
]

sales_df_big_clean = sales_df_big_clean.copy()
sales_df_big_clean["date_dirty"] = [dirty_dates[i % len(dirty_dates)] for i in range(len(sales_df_big_clean))]

# Automatic parsing approaches were tested first, but they were not reliable enough
# for this mixed-format scenario.
# sales_df_big_clean["date_clean"] = pd.to_datetime(sales_df_big_clean["date_dirty"], errors="coerce")
# sales_df_big_clean["date_clean"] = pd.to_datetime(sales_df_big_clean["date_dirty"], errors="coerce", dayfirst=True)
# sales_df_big_clean["date_clean"] = pd.to_datetime(sales_df_big_clean["date_dirty"], errors="coerce", format="mixed")
# sales_df_big_clean["date_clean"] = pd.to_datetime(sales_df_big_clean["date_dirty"], errors="coerce", format="mixed", dayfirst=True)

# Build broad masks based on separators and time markers.
slash_mask = sales_df_big_clean["date_dirty"].str.contains("/", regex=False, na=False)
dash_mask = sales_df_big_clean["date_dirty"].str.contains("-", regex=False, na=False)
dot_mask = sales_df_big_clean["date_dirty"].str.contains(".", regex=False, na=False)
time_mask = sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False)

# Build more specific masks for each supported date group.
year_dash_mask = sales_df_big_clean["date_dirty"].str.get(4).eq("-").fillna(False)
# year_dash_mask = sales_df_big_clean["date_dirty"].str.slice(4, 5).eq("-").fillna(False)

# Separate pure date formats from datetime formats.
year_dash_iso_mask = (
    sales_df_big_clean["date_dirty"].str.get(4).eq("-").fillna(False)
) & (~sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

year_dash_time_mask = (
    sales_df_big_clean["date_dirty"].str.get(4).eq("-").fillna(False)
) & (sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

day_dash_iso_mask = (
    sales_df_big_clean["date_dirty"].str.get(2).eq("-").fillna(False)
) & (~sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

day_dash_time_mask = (
    sales_df_big_clean["date_dirty"].str.get(2).eq("-").fillna(False)
) & (sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

day_slash_iso_mask = (
    sales_df_big_clean["date_dirty"].str.get(2).eq("/").fillna(False)
) & (~sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

day_slash_time_mask = (
    sales_df_big_clean["date_dirty"].str.get(2).eq("/").fillna(False)
) & (sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

day_dot_iso_mask = (
    sales_df_big_clean["date_dirty"].str.get(2).eq(".").fillna(False)
) & (~sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

year_slash_iso_mask = (
    sales_df_big_clean["date_dirty"].str.get(4).eq("/").fillna(False)
) & (~sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

year_dot_iso_mask = (
    sales_df_big_clean["date_dirty"].str.get(4).eq(".").fillna(False)
) & (~sales_df_big_clean["date_dirty"].str.contains(":", regex=False, na=False))

# Initialize control columns used during the cleaning workflow.
sales_df_big_clean["group_reviewed"] = False
sales_df_big_clean["is_ambiguous"] = False
sales_df_big_clean["invalid_date"] = False
sales_df_big_clean["safe_to_parse"] = False

# ---------------------------
# Group 1: DD/MM/YYYY (no time)
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[day_slash_iso_mask, "date_dirty"].str.slice(0, 2).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[day_slash_iso_mask, "date_dirty"].str.slice(3, 5).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = day_slash_iso_mask & (sales_df_big_clean["is_ambiguous"] == False)

sales_df_big_clean["date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%d/%m/%Y",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[day_slash_iso_mask, "group_reviewed"] = True

# ---------------------------
# Group 2: DD-MM-YYYY (no time)
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[day_dash_iso_mask, "date_dirty"].str.slice(0, 2).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[day_dash_iso_mask, "date_dirty"].str.slice(3, 5).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = day_dash_iso_mask & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%d-%m-%Y",
    errors="coerce"
)

# Flag records that may require a US-to-EU day/month swap after review.
sales_df_big_clean["US_UE_swap"] = False
sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[day_dash_iso_mask, "group_reviewed"] = True

# ---------------------------
# Group 3: DD.MM.YYYY (no time)
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[day_dot_iso_mask, "date_dirty"].str.slice(0, 2).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[day_dot_iso_mask, "date_dirty"].str.slice(3, 5).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = day_dot_iso_mask & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%d.%m.%Y",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[day_dot_iso_mask, "group_reviewed"] = True

# ---------------------------
# Group 4: YYYY-MM-DD (no time)
# Even with the year first, the day/month part can still be ambiguous.
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[year_dash_iso_mask, "date_dirty"].str.slice(8, 10).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[year_dash_iso_mask, "date_dirty"].str.slice(5, 7).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = year_dash_iso_mask & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%Y-%m-%d",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[year_dash_iso_mask, "group_reviewed"] = True

# ---------------------------
# Group 5: YYYY.MM.DD (no time)
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[year_dot_iso_mask, "date_dirty"].str.slice(8, 10).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[year_dot_iso_mask, "date_dirty"].str.slice(5, 7).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = year_dot_iso_mask & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%Y.%m.%d",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[year_dot_iso_mask, "group_reviewed"] = True

# ---------------------------
# Group 6: YYYY/MM/DD (no time)
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[year_slash_iso_mask, "date_dirty"].str.slice(8, 10).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[year_slash_iso_mask, "date_dirty"].str.slice(5, 7).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = year_slash_iso_mask & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%Y/%m/%d",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[year_slash_iso_mask, "group_reviewed"] = True

# Check which records still belong to unreviewed groups.
group_not_reviewed = sales_df_big_clean["group_reviewed"] == False
print(sales_df_big_clean.loc[group_not_reviewed, ["order_id", "date_dirty", "group_reviewed"]])

# Build masks for datetime formats:
# - DD/MM/YYYY HH:MM
# - YYYY-MM-DD HH:MM:SS
# The number of ":" characters helps separate formats with and without seconds.
day_slash_time_mask_noS = (
    sales_df_big_clean["date_dirty"].str.get(2).eq("/").fillna(False)
) & (sales_df_big_clean["date_dirty"].str.count(":") == 1)

year_dash_time_mask_full = (
    sales_df_big_clean["date_dirty"].str.get(4).eq("-").fillna(False)
) & (sales_df_big_clean["date_dirty"].str.count(":") == 2)

# ---------------------------
# Group 7: DD/MM/YYYY HH:MM
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[day_slash_time_mask_noS, "date_dirty"].str.slice(0, 2).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[day_slash_time_mask_noS, "date_dirty"].str.slice(3, 5).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = day_slash_time_mask_noS & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%d/%m/%Y %H:%M",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[day_slash_time_mask_noS, "group_reviewed"] = True

# ---------------------------
# Group 8: YYYY-MM-DD HH:MM:SS
# ---------------------------

sales_df_big_clean["first_part"] = sales_df_big_clean.loc[year_dash_time_mask_full, "date_dirty"].str.slice(8, 10).astype(int)
sales_df_big_clean["second_part"] = sales_df_big_clean.loc[year_dash_time_mask_full, "date_dirty"].str.slice(5, 7).astype(int)

sales_ambi_mask = (
    (sales_df_big_clean["first_part"] > 0) &
    (sales_df_big_clean["first_part"] < 13) &
    (sales_df_big_clean["second_part"] > 0) &
    (sales_df_big_clean["second_part"] < 13)
)
sales_df_big_clean.loc[sales_ambi_mask, "is_ambiguous"] = True

parse_mask = year_dash_time_mask_full & (sales_df_big_clean["is_ambiguous"] == False)
sales_df_big_clean.loc[parse_mask, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[parse_mask, "date_dirty"],
    format="%Y-%m-%d %H:%M:%S",
    errors="coerce"
)

sales_df_big_clean.loc[parse_mask, "US_UE_swap"] = (
    (sales_df_big_clean.loc[parse_mask, "date_clean"].isna()) &
    (sales_df_big_clean.loc[parse_mask, "first_part"] <= 12) &
    (sales_df_big_clean.loc[parse_mask, "second_part"] > 12)
)

sales_df_big_clean.loc[parse_mask, "invalid_date"] = sales_df_big_clean.loc[parse_mask, "date_clean"].isna()
sales_df_big_clean.loc[parse_mask, "safe_to_parse"] = sales_df_big_clean.loc[parse_mask, "invalid_date"] == False
sales_df_big_clean.loc[year_dash_time_mask_full, "group_reviewed"] = True

# Handle empty and unrecognized values left in date_dirty.
sales_df_big_clean[["unrecognized_format", "empty_date"]] = False

empty_group_mask = sales_df_big_clean["date_dirty"].isna()
sales_df_big_clean.loc[empty_group_mask, "invalid_date"] = True
sales_df_big_clean.loc[empty_group_mask, "empty_date"] = True
sales_df_big_clean.loc[empty_group_mask, "group_reviewed"] = True

unrecognized_group_mask = (~sales_df_big_clean["date_dirty"].isna()) & (sales_df_big_clean["group_reviewed"] == False)
sales_df_big_clean.loc[unrecognized_group_mask, "invalid_date"] = True
sales_df_big_clean.loc[unrecognized_group_mask, "unrecognized_format"] = True
sales_df_big_clean.loc[unrecognized_group_mask, "group_reviewed"] = True

# Ambiguous dates are reviewed using business context.
# Since all affected orders come from Polish cities, the European interpretation is used.
# Time values are stored separately in a dedicated time_clean column.

sales_df_big_clean["time_clean"] = None

# Review an ambiguous record with time and split datetime into date and time.
poznan_ambiguous_time_mask = (
    (sales_df_big_clean["is_ambiguous"] == True) &
    (sales_df_big_clean["city"] == "Poznan")
)

test_row = sales_df_big_clean.loc[poznan_ambiguous_time_mask].copy()
test_row["datetime_full"] = pd.to_datetime(test_row["date_dirty"], format="%d/%m/%Y %H:%M", errors="coerce")
test_row["date_only"] = test_row["datetime_full"].dt.date
test_row["time_only"] = test_row["datetime_full"].dt.time

print(sales_df_big_clean.loc[poznan_ambiguous_time_mask, "date_dirty"])

sales_df_big_clean.loc[poznan_ambiguous_time_mask, "date_clean"] = test_row["date_only"]
sales_df_big_clean.loc[poznan_ambiguous_time_mask, "time_clean"] = test_row["time_only"]
sales_df_big_clean.loc[poznan_ambiguous_time_mask, ["is_ambiguous", "invalid_date", "safe_to_parse"]] = [False, False, True]

# Review additional ambiguous records containing time.
print(sales_df_big_clean.loc[sales_df_big_clean["is_ambiguous"] == True, ["order_id", "date_dirty"]])
print(sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "date_dirty"])

sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "date_dirty"],
    format="%d/%m/%Y %H:%M",
    errors="coerce"
)
sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "time_clean"] = (
    sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "date_clean"].dt.time
)
sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "date_clean"] = (
    sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, "date_clean"].dt.date
)
sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1014, ["is_ambiguous", "invalid_date", "safe_to_parse"]] = [False, False, True]

print(sales_df_big_clean.loc[sales_df_big_clean["is_ambiguous"] == True, ["order_id", "date_dirty"]])
print(sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, ["order_id", "date_dirty"]])

sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, "date_dirty"],
    format="%Y-%m-%d %H:%M:%S",
    errors="coerce"
)
sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, "time_clean"] = (
    sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, "date_clean"].dt.time
)
sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, "date_clean"] = (
    sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, "date_clean"].dt.date
)
sales_df_big_clean.loc[sales_df_big_clean["order_id"] == 1012, ["is_ambiguous", "invalid_date", "safe_to_parse"]] = [False, False, True]

print(sales_df_big_clean.loc[sales_df_big_clean["is_ambiguous"] == True, ["order_id", "date_dirty"]])

# Resolve the remaining ambiguous records in groups based on the separator.
ambi_slash_to_clean = (
    (sales_df_big_clean["is_ambiguous"] == True) &
    (sales_df_big_clean["date_dirty"].str.contains("/", regex=False, na=False))
)
ambi_dash_to_clean = (
    (sales_df_big_clean["is_ambiguous"] == True) &
    (sales_df_big_clean["date_dirty"].str.contains("-", regex=False, na=False))
)

sales_df_big_clean.loc[ambi_slash_to_clean, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[ambi_slash_to_clean, "date_dirty"],
    format="%d/%m/%Y",
    errors="coerce"
)
sales_df_big_clean.loc[ambi_dash_to_clean, "date_clean"] = pd.to_datetime(
    sales_df_big_clean.loc[ambi_dash_to_clean, "date_dirty"],
    format="%Y-%m-%d",
    errors="coerce"
)

sales_df_big_clean.loc[ambi_slash_to_clean, ["is_ambiguous", "invalid_date", "safe_to_parse"]] = [False, False, True]
sales_df_big_clean.loc[ambi_dash_to_clean, ["is_ambiguous", "invalid_date", "safe_to_parse"]] = [False, False, True]

# Check which records still have empty date_clean after the main cleaning workflow.
print(sales_df_big_clean.loc[sales_df_big_clean["date_clean"].isna(), ["order_id", "date_dirty"]])

# Some remaining records require a more specific correction.
# order_id alone turned out not to be unique enough in all cases,
# so the US_UE_swap flag is used as an additional condition.
sales_df_big_clean.loc[
    (sales_df_big_clean["order_id"] == 1007) & (sales_df_big_clean["US_UE_swap"] == True),
    "date_clean"
] = pd.to_datetime(
    sales_df_big_clean.loc[
        (sales_df_big_clean["order_id"] == 1007) & (sales_df_big_clean["US_UE_swap"] == True),
        "date_dirty"
    ],
    format="%m-%d-%Y",
    errors="coerce"
)

sales_df_big_clean.loc[
    (sales_df_big_clean["order_id"] == 1022) & (sales_df_big_clean["US_UE_swap"] == True),
    "date_clean"
] = pd.to_datetime(
    sales_df_big_clean.loc[
        (sales_df_big_clean["order_id"] == 1022) & (sales_df_big_clean["US_UE_swap"] == True),
        "date_dirty"
    ],
    format="%m-%d-%Y",
    errors="coerce"
)

sales_df_big_clean.loc[
    (sales_df_big_clean["order_id"] == 1015) & (sales_df_big_clean["US_UE_swap"] == True),
    "date_clean"
] = pd.to_datetime(
    sales_df_big_clean.loc[
        (sales_df_big_clean["order_id"] == 1015) & (sales_df_big_clean["US_UE_swap"] == True),
        "date_dirty"
    ],
    format="%Y-%d-%m",
    errors="coerce"
)

# Keep US_UE_swap as an informational flag for later review,
# but update the final parsing status.
sales_df_big_clean.loc[sales_df_big_clean["US_UE_swap"], ["invalid_date", "safe_to_parse"]] = [False, True]

# Final control check:
# the remaining records should represent empty values, unrecognized format,
# or impossible calendar dates such as 31/02/2026.
# print(sales_df_big_clean.loc[sales_df_big_clean["date_clean"].isna(), ["order_id", "date_dirty"]])

#counting statuses of records after cleaning
#total records:
total_records= len(sales_df_big_clean)
#statuses
summary_df=pd.DataFrame({"metric":["Total records",
        "Parsed successfully",
        "Problematic records",
        "Potential initial format problem",
        "Records with extracted time",
        "Unrecognized format",
        "Empty date"],
                         "value":[len(sales_df_big_clean),
        sales_df_big_clean["safe_to_parse"].sum(),
        sales_df_big_clean["invalid_date"].sum(),
        sales_df_big_clean["US_UE_swap"].sum(),
        sales_df_big_clean["time_clean"].notna().sum(),
        sales_df_big_clean["unrecognized_format"].sum(),
        sales_df_big_clean["empty_date"].sum()]})
#Ratios
summary_df["share"]=(summary_df["value"]/total_records * 100).round(2).astype(str) + "%"

print(sales_df_big_clean.loc[sales_df_big_clean['invalid_date'],['order_id','date_dirty','empty_date','unrecognized_format','US_UE_swap']])
print(summary_df)
#creating report for discounted products assuming that 0 in discount_price will be a regular price
sales_df_big_clean["effective_discount_price"]=sales_df_big_clean["discount_price"]
sales_df_big_clean.loc[sales_df_big_clean["effective_discount_price"]==0, "effective_discount_price"]=sales_df_big_clean["price"]

sales_df_big_clean["discounted_revenue"]=sales_df_big_clean["qty"]*sales_df_big_clean["effective_discount_price"]
sales_df_big_clean["discount_loss"]= sales_df_big_clean["revenue"]-sales_df_big_clean["discounted_revenue"]
#Revenue summary by city
print("\nRevenue summary by city")
city_summary=sales_df_big_clean.groupby("city").agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),total_discount_rev=("discounted_revenue","sum")).reset_index().sort_values("total_revenue", ascending=False)
print(city_summary)
#Revenue summary by sell channel group
print("\nRevenue summary by channel group")
channel_summary=sales_df_big_clean.groupby(["city","channel_group"]).agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),total_discount_rev=("discounted_revenue","sum")).reset_index().sort_values("total_revenue", ascending=False)
print(channel_summary)
#Discount impact summary by product
discount_summary=sales_df_big_clean.groupby("product").agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),total_discount_rev=("discounted_revenue","sum"),total_discount_loss=("discount_loss","sum")).reset_index().sort_values("total_revenue", ascending=False)
discount_summary["discount_ratio"]=discount_summary.apply(lambda row: round(row["total_discount_loss"]/row["total_revenue"]*100,2), axis=1)
discount_summary_sorted=discount_summary.sort_values("discount_ratio", ascending=False)
discount_summary_sorted["discount_ratio"]=discount_summary_sorted["discount_ratio"].map(lambda x: str(x) + "%")
#Report showing the percentage impact of discounts on total revenue by product
print("\nDiscount impact summary by discount ratio")
print(discount_summary_sorted)

# print(sales_df_big_clean.groupby("product").agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),total_discount_rev=("discounted_revenue","sum"),total_discount_loss=("discount_loss","sum")).reset_index().sort_values("total_revenue", ascending=False))
# print(sales_df_big_clean.groupby("product").agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),max_price=("price","max"),min_price=("price","min")).reset_index().sort_values("total_revenue", ascending=False))
print("\nRevenue summary by product and channel group")
product_channel_summary=sales_df_big_clean.groupby(["product","channel_group"]).agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),total_discount_rev=("discounted_revenue","sum")).reset_index().sort_values("total_revenue", ascending=False)
print(product_channel_summary)
# print(sales_df_big_clean.groupby(["product","city"]).agg(total_qty=("qty","sum"),total_revenue=("revenue","sum"),total_discount_rev=("discounted_revenue","sum")).reset_index().sort_values("product", ascending=True))

# Key findings:
# 1. Krakow generated the highest total revenue, with Warsaw close behind.
#    The difference between these two cities and the rest is significant.

# 2. The revenue structure suggests that electronics products contribute strongly
#    to total sales, especially in the top-performing cities.

# 3. The city-channel summary shows strong digital sales in Krakow and strong offline sales in Warsaw.
#     This may suggest different behavior or sales structure across cities,
#     but the dataset is too small to confirm it.

# 4. Discount analysis shows the highest discount impact for Mouse,
#    which may help explain its relatively high sales quantities.