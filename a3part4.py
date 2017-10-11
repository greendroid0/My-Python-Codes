dna = input("Enter DNA sequence:")
list1 = dna.upper() 
name = list(list1)
status = 1;

for i in range(0,len(name)):
	if(name[i] != 'A' and name[i] != 'T' and name[i] != 'C' and name[i] != 'G' and status == 1):
		print("This is not a DNA base sequence",end = '')
		status = 0

if(status == 1):
	print ("Input sequence is: ",end = '')
	for i in range(0,len(name)):		
		print(list1[i],end = '')
	print("")
	print ("Compl sequence is: ",end = '')
	for i in range(0,len(name)):
		if(name[i] == 'A'):
			name[i] = 'T'
		elif(name[i] == 'T'):
			name[i] = 'A'		
		elif(name[i] == 'C'):
			name[i] = 'G'
		elif(name[i] == 'G'):
			name[i] = 'C'		
		print(name[i],end = '')
print("")
