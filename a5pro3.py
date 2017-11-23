import statistics
f = open("midgrades.txt", "r")

checounter = envcounter = matcounter = mbgcounter = phycounter = geocounter = 0 
cheexamres = envexamres = matexamres = mbgexamres = phyexamres = geoexamres = 0 
howmany = 0

che_list=[]
env_list=[]
mat_list=[]
mbg_list=[]
phy_list=[]
geo_list=[]

for line in f:
	
	department = line.split(',')[0]
	student_id = line.split(',')[1]
	exam_result = line.split(',')[2]
	howmany += 1

	if department == "CHE": 
		if int(exam_result) != 0  :
			checounter+=1
			cheexamres += int(exam_result) 
			che_list.append(int(exam_result))
		
	if department == "ENV": 
		if int(exam_result) != 0  :
			envcounter+=1
			envexamres += int(exam_result) 
			env_list.append(int(exam_result))

	if department == "MAT": 
		if int(exam_result) != 0  :
			matcounter+=1
			matexamres += int(exam_result) 
			mat_list.append(int(exam_result))

	if department == "MBG": 
		if int(exam_result) != 0  :
			mbgcounter+=1
			mbgexamres += int(exam_result)
			mbg_list.append(int(exam_result))
	
	if department == "PHY":
		if int(exam_result) != 0 :
			phycounter+=1
			phyexamres += int(exam_result)
			phy_list.append(int(exam_result))

	if department == "GEO":
		if int(exam_result) != 0 :
			geocounter+=1
			geoexamres += int(exam_result)
			geo_list.append(int(exam_result))

absence = howmany - geocounter - matcounter - envcounter - checounter - phycounter - mbgcounter

che_list.sort()
env_list.sort()
mat_list.sort()
mbg_list.sort()
phy_list.sort()
geo_list.sort()

totalexamres = cheexamres + envexamres + matexamres + mbgexamres + phyexamres + geoexamres
totalcounter = checounter + envcounter + matcounter + mbgcounter + phycounter + geocounter

print (str(absence) + " of " + str(howmany) + " people​ ​ didn't​ ​ take​ ​ the​ ​ exam.")
print ("CHE MEAN: " + str(cheexamres / checounter) + "," + " MEDIAN: " + str(round(statistics.median(che_list),1)) + " out of " + str(checounter) + " people")
print ("ENV MEAN: " + str(round((envexamres / envcounter),1)) + "," + " MEDIAN: " + str(round(statistics.median(env_list),1)) + " out of " + str(envcounter) + " people")
print ("MAT MEAN: " + str(round((matexamres / matcounter),1)) + "," + " MEDIAN: " + str(round(statistics.median(mat_list),1)) + " out of " + str(matcounter) + " people")
print ("MBG MEAN: " + str(round((mbgexamres / mbgcounter),1)) + "," + " MEDIAN: " + str(round(statistics.median(mbg_list),1)) + " out of " + str(mbgcounter) + " people")
print ("PHY MEAN: " + str(round((phyexamres / phycounter),1)) + "," + " MEDIAN: " + str(round(statistics.median(phy_list),1)) + " out of " + str(phycounter) + " people")
print ("GEO MEAN: " + str(round((geoexamres / geocounter),1)) + "," + " MEDIAN: " + str(round(statistics.median(geo_list),1)) + " out of " + str(geocounter) + " people")

print ("TOTAL MEAN: " + str(round((totalexamres / totalcounter),1)) + "," + " MEDIAN: " + str(round(statistics.median( che_list + env_list + mat_list + mbg_list + phy_list + geo_list),1)) + " out of " + str(totalcounter) + " people")
