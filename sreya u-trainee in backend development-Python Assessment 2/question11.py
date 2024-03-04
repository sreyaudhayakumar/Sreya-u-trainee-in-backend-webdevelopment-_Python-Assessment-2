"""11. Write a Python function called calculate_discounted_price that takes the
original price of an item and a discount percentage as input. The function
should return the discounted price after applying the discount. Ensure that
the function handles the case where the discount percentage is negative
and raises a custom exception called InvalidDiscountError with an
appropriate error message"""

class InvalidDiscountError(Exception):
    pass

def calculate_discounted_price(original_price, discount_percentage):
    if discount_percentage < 0:
        raise InvalidDiscountError("Discount percentage cannot be negative")
    return original_price * (1 - discount_percentage / 100)

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    print("Discounted price:", discounted_price)
except ValueError:
    print("Error: Please enter valid numeric values for price and discount percentage")
except InvalidDiscountError as e:
    print("Error:", e)

