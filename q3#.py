

rows=2
columns= int(input())
i = 0
while(i < rows):
    j = 0
    while(j < columns):
        print("#"*(columns-1), end = '  ')
        j = j + 1
    i = i + 1
    print()
