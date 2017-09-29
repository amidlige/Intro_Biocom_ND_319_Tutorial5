import pandas
wages=pandas.read_csv("wages.csv")
ed12=wages[wages.yearsSchool==12] #12 years of education
minimum12=min(ed12.wage) #minimum wage of 12
ed16=wages[wages.yearsSchool==16] #16 years of education
minimum16=min(ed16.wage) #minimum wage of 16
print (minimum16-minimum12)

