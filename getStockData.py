import csv

def getEmployeeStock(user):
	last = user.split("-")[0].upper()
	first = user.split("-")[1].upper()
	with open('enron-stock.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if(row['Name']==""):
				break
				
				
			first_name = row['Name'].split(", ")[1]
			last_name = row['Name'].split(", ")[0]
			
			if((last_name==last) and (first==first_name[0])):
				retval = row['Stock Value'].replace(",","")
				retval = retval.replace("$","")
				return (first_name,last_name,retval)
			#print(row['Name'], row['Stock Value'])
			
	return (-1,-1,-1)