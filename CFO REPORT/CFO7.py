import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file = pd.read_csv('BadIPGone.csv')

# Initialize counters
hoosiers_count = 0
department_counts = {}

# Loop through the rows
for index, row in file.iterrows():
    # Check if the customer is from Indiana (assuming 'Hoosier' refers to Indiana resident)
    if row['state'] == 'Indiana':
        hoosiers_count += 1
        # Increment the count for the department
        department = row['department']
        if department in department_counts:
            department_counts[department] += 1
        else:
            department_counts[department] = 1

# Print the number of Hoosiers who purchased items
print(f"Number of Hoosiers who purchased items: {hoosiers_count}")

# Print the breakdown of purchases by department for Hoosiers
print("Breakdown of purchases by department for Hoosiers:")
for department, count in department_counts.items():
    print(f"{department}: {count}")

# Plotting the breakdown of purchases by department for Hoosiers
plt.bar(department_counts.keys(), department_counts.values())
plt.xlabel('Department')
plt.ylabel('Number of Purchases')
plt.title('Breakdown of Purchases by Department for Hoosiers')
plt.show()