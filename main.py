# Write a small function that returns the values of an array that are not odd.
# All values in the array will be integers. Return the good values in the order
# they are given.


def no_odds(values):
    return [num for num in values if num % 2 == 0]


print(no_odds([1, 2, 3, 4, 5, 6]))
