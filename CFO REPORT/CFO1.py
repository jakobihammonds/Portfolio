import pandas as pd
file = pd.read_csv("cleandata.csv",header=0)

#find the unique departments
departments = file["department"].unique()
theDeparted=[]
for eachDepartment in departments:
    theDeparted.append(eachDepartment)
departmentsCost=[]
for i in range(len(departments)):
    departmentsCost.append(0)
    
#loop through the file
for i in range(len(file)):
    d=file["department"][i]
    c=file["cost"][i]
    indexInDepartments=int(theDeparted.index(d))
    departmentsCost[indexInDepartments]+=c

#print list
for i in range(len(departments)):
    print(f"{departments[i]}:\t${departmentsCost[i]}")
    
''' 
    For problem number 2, we could put
    theDepartment and departmentsCost in the pandas df
    sort the df
    pull the top 5 with file.head(5)
    pull the bottom 5

'''