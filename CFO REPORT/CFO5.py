import pandas as pd
file = pd.read_csv('BadIPGone.csv')

visa,mc=0,0
#loop through the card numbers
for eachCard in file['card']:
#if the first number is 4
    if str(eachCard)[0] == '4':
            visa+=1
    elif str(eachCard)[0]=="5":
        mc+=1
#else if the first number is 5
#      master+=1
print(f'''
number of visas:{visa}
number of mastercards:{mc}
''')