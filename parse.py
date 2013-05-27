#!/usr/bin/python
from string import letters

#http://opengeocode.org/download/cow.php

f = open('cow.txt', 'r')

listOfLines=list()

for line in f:
	
	if line[0]!='#':
		listOfLines.append(line)
f.close()


minLatitude=list()
maxLatitude=list()
countries = list()
countriesExt = list()


for line in listOfLines:
	aux= line.split(';')
	if len(aux)==1 or aux[-7]=="minlatitude":
		pass
	else:
		minLatitude.append(float(aux[-7]))
		maxLatitude.append(float(aux[-8]))
		countries.append(aux[0])
		countriesExt.append(aux[4])


	

a= raw_input()

latitude= float(a)

for indexCountry in range(len(countries)):
	if latitude >= minLatitude[indexCountry] and latitude <=maxLatitude[indexCountry]:
		print countriesExt[indexCountry]
		print minLatitude[indexCountry]
		print maxLatitude[indexCountry]


