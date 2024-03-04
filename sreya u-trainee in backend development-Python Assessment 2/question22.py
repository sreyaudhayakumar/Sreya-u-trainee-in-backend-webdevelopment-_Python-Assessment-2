"""22.Write a Python program input and add two integers only and handle the 
exceptions.
RUN 1:
Enter First Value: 10
Enter Second Value: 20
0.5
RUN 2:
Enter First Value: 10
Enter Second Value: Hello
Pls Input Integer Only invalid literal for int() with base 10: 'Hello'
RUN 3:
Enter First Value: 10
Enter Second Value: 0
Second Number Should Not Be Zero division by zer0"""

def operation_integers():
    try:
        num1 = int(input("Enter First Value: "))
        num2 = int(input("Enter Second Value: "))

        result = num1 / num2

        print(result)

    except ValueError:
        print("Pls Input Integer Only")
    except ZeroDivisionError:
        print("Second Number Should Not Be Zero")
operation_integers()
