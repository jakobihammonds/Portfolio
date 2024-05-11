import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file = pd.read_csv('BadIPGone.csv')

# Group by department and calculate total amount of purchase
department_purchase = file.groupby('department')['cost'].sum()

# Sort departments based on total purchase amount
department_purchase_sorted = department_purchase.sort_values(ascending=False)

# Plotting the top 5 and bottom 5 departments based on amount of purchase
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Top 5 departments
top_5 = department_purchase_sorted.head(5)
axs[0].bar(top_5.index, top_5.values, color='blue')
axs[0].set_title('Top 5 Departments based on Purchase Amount')
axs[0].set_xlabel('Department')
axs[0].set_ylabel('Total Purchase Amount')

# Bottom 5 departments
bottom_5 = department_purchase_sorted.tail(5)
axs[1].bar(bottom_5.index, bottom_5.values, color='red')
axs[1].set_title('Bottom 5 Departments based on Purchase Amount')
axs[1].set_xlabel('Department')
axs[1].set_ylabel('Total Purchase Amount')

plt.tight_layout()
plt.show()

# Calculate the spread between top and bottom departments
top_total = top_5.sum()
bottom_total = bottom_5.sum()
spread = top_total - bottom_total

print("Spread between top and bottom departments:", spread)