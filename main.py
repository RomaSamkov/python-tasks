# 8 kyu
# Combine strings function
# Create a function named combineNames/combine_names/CombineNames that accepts
# two parameters (first and last name). The function should return the full name.
#
# Example:
#
# With "James" as the first name and "Stevens"
# as the last name should return "James Stevens"

def combine_names(first, last):
    return f"{first} {last}"


print(combine_names("James", "Stevens"))


# Accountant time! For a given quantity and price (per mango),
# calculate the total cost of the mangoes.
# But! Every third mango is free!

def mango(quantity, price):
    return price * (quantity - (quantity // 3))


print(mango(3, 3))
