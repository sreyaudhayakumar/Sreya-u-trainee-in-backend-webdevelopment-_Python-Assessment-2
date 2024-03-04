"""13. Implement a program that simulates a basic calculator, allowing users to
perform arithmetic operations (addition, subtraction, multiplication,
division) on two numbers."""

value1=int(input("enter a value1:"))
value2=int(input("enter a value2:"))

operator=input("enter the opeartor:,+,-,*,/")

if operator == '+':
    print("addition of two value is:",value1+value2)
elif operator == '-':
    print("substraction of two values is:",value1-value2)
elif operator == '*':
    print("multiplication of two operator is:",value1*value1)
elif operator == '/':
    print("division of two value is:",value1/value2)
else:
    print("invalid operator")