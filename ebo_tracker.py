#! python3
# extract EBO UPS third party tracking
# data is from Quantum View Autoload WCM EBO Track data file
# Chad Cropley 2016-07-08 a RAD design solution
#

# import modules
import os
import shutil
import csv

# make sure we're in the right directory
os.chdir('c:\\Users\\chad\\AppData\\Local\\VirtualStore\\Program Files (x86)\\Ups\\Quantum View\\Autoload\\ccropley\\WCMThirdparty')
dir = os.getcwd()

# os.system('pause')

# read file1
filename = input('Enter a Quantum View UPS filename: ')

shutil.copyfile(filename, 'qviewups.csv')

# read user file and extract only necessary columns & format to make UPS file
with open(filename) as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',')
	with open('output.csv','w') as output:
		writer = csv.DictWriter(output, delimiter=',', fieldnames=reader.fieldnames)
		for row in reader:
			print(row['Tracking Number'],',',',', 'W'+row['Package Reference Number Value 1'],',',',',',', row['Package Activity Date'], file = output)			

# os.system('pause')

# Remove duplicate items from merge

inFile = open('output.csv','r')

outFile = open('output001.csv','w')

listLines = []

for line in inFile:
	if line in listLines:
		continue
	else:
		outFile.write(line)
		listLines.append(line)

outFile.close()

inFile.close()

# copy formatted file to tracking computer and append to UPS file
shutil.copyfile('output001.csv', 'z:\\output001.csv')

# Change working directory
os.chdir('z:\\')

# backup the live date b-4 modifying it
# (WCM_Track_Info - Copy.csv is test file - rename for production)
shutil.copyfile('WCM_Track_Info - Copy.csv', 'WCM_Track_Info - Copy2.csv')

with open('WCM_Track_Info - Copy.csv', 'a', newline='') as f1:
	writer = csv.writer(f1, delimiter=',')
	with open('output001.csv', 'r') as csvfile1:
		readcsv = csv.reader(csvfile1, delimiter = ',')
		for row in readcsv:
			writer.writerow(row)

print('EBO third party tracking information has been merged with UPS track file')
os.system('pause')