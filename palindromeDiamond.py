print("Input the number of rows")
n=int(input())-1


for i in range(1, n * 2 + 1):
    print(end=" ")
print("1")

for i in range(1, n * 2 ):

	if (i < n):
		for j in range(1, (n - i) * 2 + 1):
		    print(end=" ")
	else:
		for j in range(1, (i % n) * 2 + 1):
		    print(end=" ")

	if (i < n):
		for j in range(i % n + 1):
			print(j+1, end=" ")
		for j in range(i % n - 1, -1, -1):
			print(j+1, end=" ")

	
	elif (i > n):
		for j in range(n - (i - n) + 1):
			print(j+1, end=" ")
		for j in range((n - (i - n)) - 1, -1, -1):
			print(j+1, end=" ")

	else:
		for j in range(n):
			print(j+1, end=" ")
		for j in range(n, -1, -1):
			print(j+1, end=" ")

	print()

 # putting the space in last line
for i in range(0, n * 2 ):  
    print(end=" ")
print("1", end="")