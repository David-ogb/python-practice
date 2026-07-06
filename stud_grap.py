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

#function to calculate the grade
def grade_sys(scores):
    for score in scores:
        if  100 > score >= 90:
            Grade = 'A'
            return Grade
        elif 89 >= score >= 80:
            Grade = 'B'
            return Grade
        elif 79 >= score >= 70:
            Grade = 'C'
            return Grade
        elif 69 >= score >= 60:
            Grade = 'D'
            return Grade
        else:
            Grade = 'F'
            return Grade

print()
for x in range(num_stud):
    print(f"{students[x]:5}:{scores[x]:4}")