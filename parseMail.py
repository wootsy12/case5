import os


dir = "enron/maildir/"


def getUserInbox(user):

	inbox = dir+user+"/inbox/"
	usrmsg = []
	try:
		listd = os.listdir(inbox)
	except:
		return usrmsg
	for email in listd:
		msg = {}
		try:
			f = open(inbox+email,'r')
		except:
			continue
		lines = f.read().splitlines()

		i=0
		while True:

			if "Mime-Version:" in lines[i]:
				break
			if "Message-ID:" in lines[i]:
				msg['Message-ID'] = lines[i].split("Message-ID: ")[1]

			elif "Date:" in lines[i]:
				msg['Date'] = lines[i].split("Date: ")[1]
			elif "From:" in lines[i]:
				msg['From'] = lines[i].split("From: ")[1]
			elif "To:" in lines[i]:
				msg['To'] = lines[i].split("To: ")[1]
			elif "Subject:" in lines[i]:
				msg['Subject'] = lines[i].split("Subject: ")[1]
			elif "\t" in lines[i]:
				try:
					msg['To'] = msg['To'] + lines[i].split("\t")[1]
				except:
					break
			
			i+=1
		while True:
			if lines[i]=="":
				break
			i+=1
		content = ''.join(lines[i:len(lines)])
		msg['Content'] = content
		usrmsg.append(msg)
		#print(content)
	return usrmsg

def getUserOutbox(user):

	inbox = dir+user+"/sent/"
	usrmsg = []
	for email in os.listdir(inbox):
		msg = {}
		try:
			f = open(inbox+email,'r')
		except:
			continue
		lines = f.read().splitlines()

		i=0
		while True:

			if "Mime-Version:" in lines[i]:
				break
			if "Message-ID:" in lines[i]:
				msg['Message-ID'] = lines[i].split("Message-ID: ")[1]

			elif "Date:" in lines[i]:
				msg['Date'] = lines[i].split("Date: ")[1]
			elif "From:" in lines[i]:
				msg['From'] = lines[i].split("From: ")[1]
			elif "To:" in lines[i]:
				msg['To'] = lines[i].split("To: ")[1]
			elif "Subject:" in lines[i]:
				msg['Subject'] = lines[i].split("Subject: ")[1]
			elif "\t" in lines[i]:
				msg['To'] = msg['To'] + lines[i].split("\t")[1]
			
			i+=1
		while True:
			if lines[i]=="":
				break
			i+=1
		content = ' '.join(lines[i:len(lines)])
		msg['Content'] = content
		usrmsg.append(msg)
		#print(content)
	return usrmsg
	
