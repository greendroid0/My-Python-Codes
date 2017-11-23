f = open("midgrades.txt", "r")
gtu_id = input('Enter​ ​ your​ ​ GTU​ ​ ID​ ​ Number:')

for line in f:
	current_student_id = line.split(',')[1]
	exam_result = line.split(',')[2].strip()
	
	if current_student_id == gtu_id:
		print ("You​ ​ got​ " + exam_result + " from​ ​ the​ ​ exam.")
		break	
			

#open the file
#firstline = readline()
#firtsline.split()
