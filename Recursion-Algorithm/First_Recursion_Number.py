def RecurringCharacter(myList):
	non_duplicates = []
	for i in myList:
		if i in non_duplicates:
			return i
		else:
			non_duplicates.append(i)
	return 'Undefined'


print(RecurringCharacter([2,1,1,2,3,4,5]))