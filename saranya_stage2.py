#Stage 2: Add Result Check
#Extend Stage 1: After showing result, check if it's positive, negative, or zero and print accordingly.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# op = input("Enter the operator: ")

# if op=="+":
#     result = num1 + num2
#     print(f'{num1} + {num2} = {result}')
# elif op=="-":
#     result = num1-num2
#     print(f'{num1} - {num2} = {result}')
# elif op=="/" and num2 != 0:
#         result = num1/num2
#         print(f'{num1} / {num2} = {result}')
# else:
#     result = num1*num2
#     print(f'{num1} * {num2} = {result}')

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

if result == 0:
    print("Zero")
elif result > 0:
     print("Positive")
else:
     print("Negative")