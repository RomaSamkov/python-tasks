# 8 kyu  Double Char 
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
def double_char(s):
    result = ''
    for char in s:
        result += char * 2
    return result

print(double_char("String"))

# 8 kyu Sum Mixed Array
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.
def sum_mix(arr):
    total_sum = 0
    for num in arr:
        total_sum += int(num)
    return total_sum

print(sum_mix([9, 3, '7', '3']))

# 8 kyu Third Angle of a Triangle
# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
def other_angle(a, b):
    # total_angle = 180
    # third_angle = total_angle - (a+b)
    return 180 - (a+b)

print(other_angle(30, 60))

# 8 kyu Exclamation marks series #1: Remove an exclamation mark from the end of string
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
def remove(s):
    return s.removesuffix('!') 

print(remove("Hi!"))