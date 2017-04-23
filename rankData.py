import os
import operator
import parseMail
from getStockData import getEmployeeStock

dir = "enron/maildir/"

uniqueRank = {}

for user in os.listdir(dir):
	print(user)
	senders = []
	
	inb = parseMail.getUserInbox(user)
	for msg in inb:
		sender = msg['From']
		try:
			domain = sender.split("@")[1]
		except:
			continue
		if(domain=="enron.com"):
			senders.append(sender)
			
	senders = list(set(senders))
	uniqueRank[user] = len(senders)

sorted = sorted(uniqueRank.items(), key=operator.itemgetter(1))

sorted.reverse()

for name in sorted:
	employee = name[0]
	rank = name[1]

	first_name, last_name, stockValue = getEmployeeStock(employee)
	if(stockValue==-1):
		continue
		
	print("Employee name: " + first_name + " " + last_name)
	print("Employee Rank: " + str(rank))
	print("Employee Stock Value: " + stockValue)
	print("\n")