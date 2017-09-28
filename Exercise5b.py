with open('wages.csv','r') as f:
    file=f.readlines()
import pandas
wages=pandas.read_csv("wages.csv")
a=wages.max(axis=0)
b=wages.min(axis=0)
print (a,b)