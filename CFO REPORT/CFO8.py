import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file = pd.read_csv('BadIPGone.csv')

# Group by customer and calculate total spending
customer_spending = file.groupby('index')['cost'].sum()

# Get the top 3 purchasers
top_3_purchasers = customer_spending.nlargest(3)

# Plotting the total spending of the top 3 purchasers
top_3_purchasers.plot(kind='bar')
plt.xlabel('Customer ID')
plt.ylabel('Total Spending')
plt.title('Total Spending of Top 3 Purchasers')
plt.show()

# Get the top departments for each of the top 3 purchasers
top_departments = {}
for customer_id in top_3_purchasers.index:
    customer_data = file[file['index'] == customer_id]
    top_department = customer_data['department'].value_counts().idxmax()
    top_departments[customer_id] = top_department

# Count occurrences of each department for the top 3 purchasers
department_counts = pd.Series(top_departments.values()).value_counts()

# Plotting the top departments for each of the top 3 purchasers as a pie chart
labels = [f'{dept} (Customer ID: {customer_id})' for customer_id, dept in top_departments.items()]
sizes = department_counts.values

plt.pie(sizes, labels=labels)
plt.axis('equal')
plt.title('Top Departments of Top 3 Purchasers')
plt.show()

# Print the top 3 purchasers, their total spending, and their top departments
print("Top 3 Purchasers:")
for customer_id, spending in top_3_purchasers.items():
    print(f"Customer ID: {customer_id}, Total Spending: {spending}, Top Department: {top_departments[customer_id]}")
