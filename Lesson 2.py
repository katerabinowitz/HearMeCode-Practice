###Lists

attendees=['Shannon','Jenn','Grace']
print attendees[0:2]
#print attendees[3] IndexError:List index out of range
print len(attendees)
attendees_ages=[]
attendees_ages.append(28)
attendees_ages.append(27)
print attendees_ages
attendees_ages[0]=29
print attendees_ages

days_of_week=["Monday","Tuesday"]
print days_of_week
days_of_week.append("Wednesday")
print days_of_week
days_of_week.append("Thursday")
print days_of_week
days_of_week.append("Friday")
print days_of_week
days_of_week.append("Saturday")
print days_of_week
days_of_week.append("Sunday")
print days_of_week

day=days_of_week.pop()
print day
print days_of_week
day=days_of_week.pop()
print day
days_of_week.append(day)
print days_of_week
day=days_of_week.pop(3)
print day
print days_of_week

months=['January','February']
print months
months.extend(['March','April','May','June','July','August','September','October','November','December'])
print months
months.pop(0)
print months
months.insert(0, 'January')
print months

address="1133 19th Street NW Washington, DC 20036"
address_as_list=address.split(" ")
print address_as_list

Ask for an address
address=raw_input("What is your address? ")
address=address.split(" ")

#Does this address have a quadrant
if "NW" in address.upper():
	NW.append(address)
elif "NE" in address.upper():
	NE.append(address)
elif "SE" in address.upper():
	SE.append(address)
elif "SW" in address.upper():
	SW.append(address)
else:
	print "No quadrant found for this address: {0}".format(address)

###For Loops

print range (10)
print range (10,20,2)
days_of_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months_of_year=['January','February']
#for number in range (6):
#	print number

for month in months_of_year:
	print "\n\n\n", month
	for week in range (1,5):
		print "It is week #{0}:".format(week)
		for day in days_of_week:
			print '\t', day

attendees=['A','B','C','D']
for seat_number, each_attendees in enumerate(attendees):
	print "My name is {0} and my number is {1}".format(each_attendees,seat_number)

bread=5
while bread>=2:
	print "I'm making a sandwich"
	bread=bread-2
else: 
	print "Not enough bread for more sandwiches :("

for abbrev,statename in zip(abbrevs, state_names):
	print "{0}'s state abbreviation is {1}.".format(state_name,abbrev)		