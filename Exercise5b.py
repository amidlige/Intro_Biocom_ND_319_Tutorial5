import pandas
wages=pandas.read_csv("wages.csv")
a=(wages.sort_values(by='wage'))
print (a.head(n=1))
print (a.tail(n=1))
