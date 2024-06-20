# 8 kyu  Double Char 
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
def double_char(s):
    result = ''
    for char in s:
        result += char * 2
    return result

# print(double_char("String"))

# 8 kyu Sum Mixed Array
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.
def sum_mix(arr):
    total_sum = 0
    for num in arr:
        total_sum += int(num)
    return total_sum

# print(sum_mix([9, 3, '7', '3']))

# 8 kyu Third Angle of a Triangle
# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
def other_angle(a, b):
    # total_angle = 180
    # third_angle = total_angle - (a+b)
    return 180 - (a+b)

# print(other_angle(30, 60))

# 8 kyu Exclamation marks series #1: Remove an exclamation mark from the end of string
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
def remove(s):
    return s.removesuffix('!') 

# print(remove("Hi!"))

# 8 kyu Is it a palindrome?
# Write a function that checks if a given string (case insensitive) is a palindrome.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the 
# same backwards as forwards, such as madam or racecar.
def is_palindrome(s):
    s = s.lower()
    reversed_s = s[::-1]
    return s == reversed_s

# print(is_palindrome('aba'))

# 8 kyu Difference of Volumes of Cuboids
# In this simple exercise, you will create a program that will take two lists of integers, a and b. 
# Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. 
# You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 
# and the volume of b is 20. Therefore, the function should return 8.
# Your function will be tested with pre-made examples as well as random ones.
def find_difference(a, b):
    volume_a = a[0]*a[1]*a[2]
    volume_b = b[0]*b[1]*b[2]
    return abs(volume_a - volume_b) 

# print(find_difference([3, 2, 5], [1, 4, 4]))

# 8 kyu Plural
# We need a simple function that determines if a plural is needed or not. 
# It should take a number, and return true if a plural should be used with that number or false if not. 
# This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
def plural(n):
    return n != 1

# print(plural(1))

# 8 kyu altERnaTIng cAsE <=> ALTerNAtiNG CaSe
#  each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. 
def to_alternating_case(string):
    return string.swapcase()


print(to_alternating_case("hello WORLD"))
