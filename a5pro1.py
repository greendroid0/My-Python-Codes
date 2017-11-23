F = "CATAGCGGTCAGAGGATAAATCCATACTTTCTTCCTCCTGTCGTATTTAA"
A = "TTCGGGTGAAGTGTCGACTATGTCACGTTTGAACGGAAGTCCTAGCTAAT"
B = "ATACCGCTAATAGCCTACTTCGGGACTGGCTTCAAAGCCGACCATGAATG"
C = "ACAGTCATTACTCGTAAATCGGTCATCTTACGTAAGTGGTATATATTTAA"
D = "GAAGCCGGTCAGAGGATAAATTCCTACTTTATTGCTCCTGTCGTATTCGT"
E = "TCGGTCAGGTCTCACTATTTGTAACATCTATTCTCAATTCGCATACTCAA"

dnaLength = len(F)
match = [0, 0, 0, 0, 0]
dnas = [A, B, C, D, E]
names = ['A', 'B', 'C', 'D', 'E']

for i in range(len(dnas)):
	for j in range (dnaLength):
		if dnas[i][j] == F[j]:
			match[i] += 1

matchPercentage  = [0, 0, 0, 0, 0]
for i in range(len(matchPercentage)):
	matchPercentage[i] = match[i] / dnaLength * 100

	if matchPercentage[i] >= 75:
		print("%" + str(round(matchPercentage[i],1)) +" with " + names[i] + "." +" Possibly your child")
		
	else:
		print("%" + str(round(matchPercentage[i],1)) +" with " + names[i] + "." +" Not your child")
	



