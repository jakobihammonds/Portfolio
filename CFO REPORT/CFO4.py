import pandas as pd

file = pd.read_csv("BadIPGone.csv", header=0)

departments_numpy = file["department"].unique()
departments = {}
for dept in departments_numpy:
    departments[dept] = 0

student_count = 0
student_cost = 0
# loop through the emails
for i in range(len(file)):
    department = file["department"][i]
    cost = file["cost"][i]
    email = file["email"][i]

    if email[len(email)-3:] == "edu":
        student_count += 1
        student_cost += cost

        departments[department] += cost

print(f"Number of student purchases: {student_count}")
print(f"Total spent by students: ${student_cost:.2f}")
for k in departments:
    print(f"{k}:\t${departments[k]:.2f}")