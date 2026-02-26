#Stage 1: Basic Calculator

#Create a calculator that takes two numbers and an operator (+,-,*,/) and shows the result.
#Constraints:
#Handle division by zero
#Use if-elif-else statements

#Example:
#Input: 10,5,+
#Output: Result = 15

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator: ")

if op=="+":
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
elif op=="-":
    result = num1-num2
    print(f'{num1} - {num2} = {result}')
elif op=="/":
    if num2 == 0:
        result = "Undefined"
        print(f'Divisible by zero is {result}')
    else:
        result = num1/num2
        print(f'{num1} / {num2} = {result}')
else:
    result = num1*num2
    print(f'{num1} * {num2} = {result}')
