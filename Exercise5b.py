import pandas
wages=pandas.read_csv("wages.csv")
wages.drop([col for col in wages.columns if 'yearsSchool' in col],axis=1,inplace=True)
cc=(wages.sort_values(by='wage'))
print ("Lowest earner")
print (cc.head(n=1))
print ("Highest Earner")
print (cc.tail(n=1))
print ("Top 10 Female Earners")
d=(wages.sort_values(by='gender'))
gender=line[0]
exp=line[1]
wage=line[3]
if 'gender'=='female':
    a=gender+' '+exp+' '+wage+' '+'\n'
print (a.tail(n=10))
    
