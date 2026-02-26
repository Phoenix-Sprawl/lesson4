#Stage 3: Student Grade Calculator
#Task: Calculate student grade based on marks in 3 subjects.

#Input: Student name, 3 subject marks (0-100)

#Calculate:
#Total marks
#Percentage=(total/300)*100

#Grade Logic:
# A: >= 75%
# B: >= 60%
# C: >= 40%
# F: < 40%

# Output: Name, Total, Percentage, Grade

student_name = input("Enter student name:")
sub1 = float(input("Enter subject1 mark: "))
sub2 = float(input("Enter subject2 mark: "))
sub3 = float(input("Enter subject3 mark: "))
total = round(sub1+sub2+sub3)
print(f'Total: {total}/300')
percentage = round((total/300)*100,1)
print(f'Percentage: {percentage}%')

if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >=40:
    print("Grade: C")
else:
    print("Grade: F")
