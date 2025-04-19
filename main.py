# ==============================
# MODE ANALYSIS USING PANDAS
# ==============================

# Step 1: Import required libraries
import pandas as pd                  # For data handling
import matplotlib.pyplot as plt      # For visualization
import statistics                    # For calculating statistical measures

# Step 2: Load the dataset
# Make sure 'Online.csv' is in the same directory or provide full path
df = pd.read_csv("Online.csv")

# Step 3: Calculate the mode (most frequent value) for selected columns

# 3.1 Mode of 'Price per Unit'
price_data = df["Price per Unit"].dropna()  # Remove missing values
mode_price = statistics.mode(price_data)

# 3.2 Mode of 'Product'
product_data = df["Product"].dropna()
mode_product = statistics.mode(product_data)

# 3.3 Mode of 'Country'
country_data = df["Country"].dropna()
mode_country = statistics.mode(country_data)

# Step 4: Display mode results
print("========== Mode Results ==========")
print(f"🪙 Mode of 'Price per Unit'      : {mode_price}")
print(f"📦 Most Frequent Product         : {mode_product}")
print(f"🌍 Most Common Customer Country  : {mode_country}")
print("==================================\n")

# Step 5: Visualize Top 5 Most Purchased Products

# 5.1 Count frequency of each product and get top 5
top_products = df["Product"].value_counts().head(5)

# 5.2 Plot bar chart
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='skyblue', edgecolor='black')

# 5.3 Customize plot
plt.title('Top 5 Most Frequently Purchased Products', fontsize=14)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Number of Purchases', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Step 6: Show plot
plt.show()
