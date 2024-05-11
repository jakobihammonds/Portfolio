import pandas as pd

# Read the CSV file
file = pd.read_csv('BadIPGone.csv')

# Initialize counters for Baby and Toy department phone numbers
baby_department_numbers = []
toy_department_numbers = []

# Loop through the rows
for index, row in file.iterrows():
    # Check if the department is Baby or Toy
    if row['department'] == 'Baby':
        baby_department_numbers.append(row['phoneNumber'])
for index, row in file.iterrows():
    if row['department'] == 'Toys':
        toy_department_numbers.append(row['phoneNumber'])

# Print the compiled lists
print("Phone numbers of customers who purchased items from the Baby department:")
print(baby_department_numbers)

print("\nPhone numbers of customers who purchased items from the Toy department:")
print(toy_department_numbers)