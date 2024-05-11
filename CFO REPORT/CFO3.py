import pandas as pd

def ipRemover():
    file=pd.read_csv("cleandata.csv",header=0)

    print(file)

    badones=[0,127,192,225]

    rowNumber=0
    for eachIP in file["ip"]:
        ipNumbers=eachIP.split(".")
        theFirstDigit=ipNumbers[0]
        if int(theFirstDigit) in badones:
            file=file.drop(lables=rowNumber,axis=0)
        rowNumber+=1

    print(file.size)
    print(file)

    file.to_csv("BadIPGone.csv",sep=',', encoding='utf-8')