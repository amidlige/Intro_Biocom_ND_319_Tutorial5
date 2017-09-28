import pandas
wages=pandas.read_csv("wages.csv")
wages.drop([col for col in wages.columns if 'yearsSchool' in col],axis=1,inplace=True)
a=(wages.sort_values(by='wage'))
print ("Lowest earner")
print (a.head(n=1))
print ("Highest Earner")
print (a.tail(n=1))
b=(wages.sort_values(by='gender','wage',ascending=False))
