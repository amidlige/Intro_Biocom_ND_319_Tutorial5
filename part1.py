import os

with open('wages.csv','r') as f:
	file = f.readlines()




for line in file:
	line = line.split(',')
	gender = line[0]
	exp = line[1]
	str = gender + ' ' + exp + '\n'
	with open('new.txt', 'a') as n:
		n.write(str)

