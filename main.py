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