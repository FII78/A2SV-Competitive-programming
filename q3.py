
# Online Python - IDE, Editor, Compiler, Interpreter
row=5
for i in range(0,row+1):
    for j in range(i,row+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
