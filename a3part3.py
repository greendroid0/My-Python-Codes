num = input("Enter a number:")
num = int(num)
print("Divisors of",num,"are: ")
for i in range(1,num):
	if (num % i == 0):
		print(i,end=' ')	
print(num) 
		
