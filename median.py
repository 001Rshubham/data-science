# Import required libraries
import pandas as pd                      # For handling CSV data
import matplotlib.pyplot as plt          # For plotting graphs
import statistics                        # For calculating median

# Load the dataset from the CSV file
# Make sure 'Online.csv' is in the same directory or provide the full path
df = pd.read_csv("Online.csv")

# Step 1: Extract the 'Price per Unit' column
# dropna() ensures we exclude any missing (NaN) values from the analysis
price_data = df["Price per Unit"].dropna()

# Step 2: Calculate the median of 'Price per Unit'
# This gives the central value of the sorted price list
median_price = statistics.median(price_data)

# Print the calculated median to the console
print(f"Median Price per Unit: {median_price}")

# Step 3: Create a histogram to visualize the distribution of prices
plt.figure(figsize=(10, 6))  # Set the size of the plot
plt.hist(price_data, bins=15, color='skyblue', edgecolor='black')  # Plot the histogram with bins and colors

# Step 4: Add a vertical dashed red line to mark the median value
plt.axvline(median_price, color='red', linestyle='dashed', linewidth=2, label=f'Median: {median_price}')

# Step 5: Add plot details
plt.title('Distribution of Price per Unit')         # Title of the plot
plt.xlabel('Price per Unit')                        # Label for x-axis
plt.ylabel('Frequency')                             # Label for y-axis
plt.legend()                                        # Show legend with median value
plt.grid(True)                                      # Add grid lines for readability
plt.tight_layout()                                  # Adjust layout to avoid clipping

# Step 6: Display the plot
plt.show()



