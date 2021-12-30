print("Enter the number of rows")
row = int(input())
col = 3

print("Rectangular pattern is: ")
for i in range(1,row+1):
    if i%2!=0:
        for j in range(1,col+1):
            print("#" *(col-1), end="  ")
    else:
        for j in range(1,col+1):
            print("  ", end="#" *(col-1))
    print()