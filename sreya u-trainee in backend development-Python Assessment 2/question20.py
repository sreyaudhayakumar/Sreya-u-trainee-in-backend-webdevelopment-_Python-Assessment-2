"""20.Create a Python library with the function to input the values with
expectation handling and demonstrate with the example"""


def input_with_handling(prompt, data_type):

    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    age = input_with_handling("Please enter your age: ", int)
    print("Your age is:", age)

    weight = input_with_handling("Please enter your weight (kg): ", float)
    print("Your weight is:", weight)
