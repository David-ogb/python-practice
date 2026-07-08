#Program to keep track of student scores

#Ask for student number
#Ask for student name and score

#Store each information to use later
#print them later

#higest score
#lowest score
#average score

#Grade each student
"""90 - 100 : A
80 - 89  : B
70 - 79  : C
60 - 69  : D
Below 60 : F"""

#function to calculate the grade
def get_grade(num):
    if 100 > num >= 90:  
        return 'A' 
    elif 89 >= num >= 80: 
        return 'B'
    elif 79 >= num >= 70: 
        return 'C' 
    elif 69 >= num >= 60: 
        return 'D'
    else: 
        return 'F'    

grades = []
students = []
scores = []
#list the number of students
num_stud = int(input("How many students? "))

#looping the names with the number of students
for x in range(num_stud):
    #Students name and score intake
    student = input("Student name: ")
    score = int(input(f"{student}'s score: "))
    # adding them both to a list
    students.append(student)
    scores.append(score)

print("\n------- REPORT ---------\n")

# a loop to print the list of students and names together
for x in range(num_stud): #number of students = number of times to run
   print(f"{students[x]:9}: {scores[x]}")

print(f"\nHighest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores)/len(scores):.2f}")
   
# looping throught the numbers and getting the grades and adding them to the grades list.
for x in range(num_stud):
    grade = get_grade(scores[x])
    grades.append(grade)
    print (f"{students[x]}, {scores[x]}, {grades[x]}")
