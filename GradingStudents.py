
# Online Python - IDE, Editor, Compiler, Interpreter

def gradingStudents(grades):
    # Write your code here
    roundedGrades=[]
    for grade in grades:
        if grade < 38:
            roundedGrades.append(grade)
        elif grade % 5 < 3:
            roundedGrades.append(grade)
        elif grade % 5 >= 3:
            add= 5 - grade % 5
            roundedGrades.append(grade+add)
        else:
            continue    
    return roundedGrades        
