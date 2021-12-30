
# Online Python - IDE, Editor, Compiler, Interpreter

n=4
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(2*(n-i-1)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()