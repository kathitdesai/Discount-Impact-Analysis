import pandas as pd

# Display settings
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", None)

# Load the dataset from Google Drive
file_id = "1ikAnWpkyDz15oG_RlKDdGZzqTpjECFTD"  # Your actual file ID
file_url = f"https://drive.google.com/uc?id={file_id}"
a = pd.read_csv(file_url)

# Sort by multiple columns
a = a.sort_values(by=["customer_id", "discount_applied"])

# Identify repeating and non-repeating customers
customer_counts = a["customer_id"].value_counts()
repeating_customers = set(customer_counts[customer_counts > 1].index)  # Customers appearing more than once
non_repeating_customers = set(customer_counts[customer_counts == 1].index)  # Customers appearing once

# Filter the dataset
repeating_data = a[a["customer_id"].isin(repeating_customers)]
non_repeating_data = a[a["customer_id"].isin(non_repeating_customers)]

# Function to calculate % increase in order count and count of rows meeting the condition
def calculate_order_count_increase(df):
    grouped = df.groupby("discount_applied").apply(lambda x: pd.Series({
        "% customers having more order_count_after": ((x["order_count_after"] > x["order_count_before"]).sum() / len(x)) * 100,
        "Count": (x["order_count_after"] > x["order_count_before"]).sum()
    }))
    return grouped

# Function to calculate % increase in total spend
def calculate_total_spend_increase(df):
    grouped = df.groupby("discount_applied").apply(lambda x: pd.Series({
        "% % customers having more total_spend_after": ((x["total_spend_after"] > x["total_spend_before"]).sum() / len(x)) * 100,
        "Count Total Spend": (x["total_spend_after"] > x["total_spend_before"]).sum()
    }))
    return grouped

# Compute percentage increases for repeating customers
repeating_order_count_increase = calculate_order_count_increase(repeating_data)
repeating_total_spend_increase = calculate_total_spend_increase(repeating_data)

# Compute percentage increases for non-repeating customers
non_repeating_order_count_increase = calculate_order_count_increase(non_repeating_data)
non_repeating_total_spend_increase = calculate_total_spend_increase(non_repeating_data)

# Merge results into separate DataFrames
repeating_result_df = repeating_order_count_increase.join(repeating_total_spend_increase)
non_repeating_result_df = non_repeating_order_count_increase.join(non_repeating_total_spend_increase)

# Add total repeating and non-repeating customer counts
repeating_customer_count = len(repeating_data)
non_repeating_customer_count = len(non_repeating_data)

# Add count per discount applied
repeating_result_df.index = [f"{idx} ({len(repeating_data[repeating_data['discount_applied'] == idx])})" for idx in repeating_result_df.index]
non_repeating_result_df.index = [f"{idx} ({len(non_repeating_data[non_repeating_data['discount_applied'] == idx])})" for idx in non_repeating_result_df.index]

# Display the results in console
print(f"Repeating Customers Analysis ({len(a) - non_repeating_customer_count})")
print(repeating_result_df)
print(f"\nNon-Repeating Customers Analysis ({non_repeating_customer_count})")
print(non_repeating_result_df)
