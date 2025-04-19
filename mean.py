
# 📦 Import required libraries
import pandas as pd                     # For data manipulation and analysis
import numpy as np                     # For numerical operations (not directly used here but often helpful)
import seaborn as sns                  # For advanced visualization
import matplotlib.pyplot as plt   # For plotting charts

# 📂 Load the dataset from a CSV file
# Make sure the path is correct and file exists at this location

data = pd.read_csv(r"C:\Users\hp\OneDrive\Pictures\Desktop\Online.csv")

# 👀 Display the first row of the DataFrame to preview the data
print(data.head(1))

# 🏷️ Print all column names to understand available features
print(data.columns)

# 🧮 Calculate the Mean and Median of the "Age" column

mean_age = data["Age"].mean()     # Average age of users
median_age = data["Age"].median() # Middle value of age distribution

# 🖨️ Print the results to the console

print("Mean Age:", mean_age)
print("Median Age:", median_age)

# 📊 Create a histogram of the Age column using seaborn

sns.histplot(
    data=data,         # Data source
    x="Age",           # Column to plot on x-axis
    bins=10,           # Number of bins/groups in histogram
    kde=True,          # Add a KDE curve to show distribution
    color="skyblue"    # Color of the bars
)




# ➕ Add a red dashed vertical line to indicate the mean
plt.axvline(
    mean_age, 
    color='red', 
    linestyle='--', 
    linewidth=2, 
    label=f'Mean: {mean_age:.1f}'
)

# ➕ Add a green solid vertical line to indicate the median

plt.axvline(
    median_age, 
    color='green', 
    linestyle='-', 
    linewidth=2, 
    label=f'Median: {median_age:.1f}'
)

# 🏷️ Add title and axis labels for clarity

plt.title("Distribution of Age")      # Title of the chart
plt.xlabel("Age")                    # Label for x-axis
plt.ylabel("Frequency")              # Label for y-axis
plt.legend()                         # Show legend with mean and median labels

# 👁️ Display the final plot

plt.show()

