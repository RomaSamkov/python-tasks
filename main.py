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
    return 180 - (a + b)


# print(other_angle(30, 60))

# 8 kyu Exclamation marks series #1: Remove an exclamation mark from the end of string Remove an exclamation mark
# from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to
# verify it.
def remove(s):
    return s.removesuffix('!')


# print(remove("Hi!"))

# 8 kyu Is it a palindrome?
# Write a function that checks if a given string (case-insensitive) is a palindrome.
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
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of an is 12
# and the volume of b is 20. Therefore, the function should return 8.
# Your function will be tested with pre-made examples as well as random ones.
def find_difference(a, b):
    volume_a = a[0] * a[1] * a[2]
    volume_b = b[0] * b[1] * b[2]
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


# print(to_alternating_case("hello WORLD"))

# 8 kyu What is between?
# Complete the function that takes two integers (a, b, where a < b)
# and return an array of all integers between the input parameters, including them.
def between(a, b):
    return list(range(a, b + 1))


# print(between(1, 4))

# 8 kyu Beginner Series #1 School Paperwork
# Your classmates asked you to copy some paperwork for them.
# You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m


# print(paperwork(-5, 5))

# 8 kyu Find the first non-consecutive number
# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive
# but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers.
# The numbers will also all be unique and in ascending order. The numbers could be positive
# or negative and the first non-consecutive could be either too!
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None


# print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))

# 8 kyu Convert to Binary
# Given a non-negative integer n, write a function to_binary/ToBinary which returns
# that number in a binary format.
def to_binary(n):
    return int(bin(n)[2:])


# print(to_binary(5))

# 7 kyu Beginner Series #3 Sum of Numbers
# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and return it.
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!
def get_sum(a, b):
    min_num = min(a, b)
    max_naum = max(a, b)

    n = max_naum - min_num + 1
    total_sum = n * (min_num + max_naum) // 2
    return total_sum


# print(get_sum(0, 1))

# 8 kyu Reversing Words in a String
# You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unnecessary whitespace.
def reverse(st):
    reverse_word = st.split()[::-1]
    return ' '.join(reverse_word)


# print(reverse('Hello World'))

# 7 kyu Number of People in the Bus There is a bus moving in the city which takes and drops some people at each bus
# stop. You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of
# people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a
# bus stop. Your task is to return the number of people who are still on the bus after the last bus stop (after the
# last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside
# the bus, they are probably sleeping there :D Take a look on the test cases. Please keep in mind that the test cases
# ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative. The second
# value in the first pair in the array is 0, since the bus is empty in the first bus stop.
def number(bus_stops):
    people_on_bus = 0
    for on, off in bus_stops:
        people_on_bus += on
        people_on_bus -= off
    return people_on_bus


# print(number([[10, 0], [3, 5], [5, 8]]))

# 8 kyu Remove exclamation marks
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    return s.replace('!', '')


# print(remove_exclamation_marks("Hello World!"))

# 8 kyu Student's Final Grade Create a function finalGrade, which calculates the final grade of a student depending
# on two parameters: a grade for the exam and a number of completed projects. This function should take two
# arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above); This
# function should return a number (final grade). There are four types of final grades: 100, if a grade for the exam
# is more than 90 or if a number of completed projects more than 10. 90, if a grade for the exam is more than 75 and
# if a number of completed projects is minimum 5. 75, if a grade for the exam is more than 50 and if a number of
# completed projects is minimum 2. 0, in other cases
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


# print(final_grade(100, 12))

# 8 kyu Add Length What if we need the length of the words separated by a space to be added at the end of that same
# word and have it returned as an array? Your task is to write a function that takes a String and returns an
# Array/list with the length of each word added to each element .
def add_length(str_):
    words = str_.split()
    result = [f"{word} {len(word)}" for word in words]
    return result


# print(add_length('apple ban'))

# 8 kyu Hello, Name or World! Define a method hello that returns "Hello, Name!" to a given name, or says Hello,
# World! if name is not given (or passed as an empty String). Assuming that name is a String, and it checks for user
# typos to return a name with a first capital letter (Xxxx).
def hello(name=""):
    if name:
        return f"Hello, {name.capitalize()}!"
    else:
        return "Hello, World!"


# print(hello("aLIce"))

# 7 kyu Sort array by string length Write a function that takes an array of strings as an argument and returns a
# sorted array containing the same strings, ordered from shortest to longest. For example, if this array were passed
# as an argument: ["Telescopes", "Glasses", "Eyes", "Monocles"] Your function would return the following array: [
# "Eyes", "Glasses", "Monocles", "Telescopes"] All the strings in the array passed to your function will be
# different lengths, so you will not have to decide how to order multiple strings of the same length.
def sort_by_length(arr):
    return sorted(arr, key=len)


# print(sort_by_length(["beg", "life", "i", "to"]))

# 8 kyu Grasshopper - Messi Goals
# Messi's Goal Total
# Use variables to find the sum of the goals Messi scored in 3 competitions
# Information
# Messi goal scoring statistics:
# Competition	Goals
# La Liga	43
# Champions League	10
# Copa del Rey	5
# Task
# Create these three variables and store the appropriate values using the table above:
# la_liga_goals
# champions_league_goals
# copa_del_rey_goals
# Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year.
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5


def goals(la_liga_goals, champions_league_goals, copa_del_rey_goals):
    total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
    return total_goals


# print(goals(43, 10, 5))

# 8 kyu You only need one - Beginner
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.
def check(seq, elem):
    return elem in seq


# print(check([66, 101], 66))


# 8 kyu Grasshopper - Basic Function Fixer
# Fix the function I created this function to add five to any number that
# was passed in to it and return the new value. It doesn't throw any errors, but it returns the wrong number.
def add_five(num):
    total = num + 5
    return total


# print(add_five(5))

# 7 kyu Two to One
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string,
# the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
def longest(a1, a2):
    combined_set = set(a1 + a2)
    result = "".join(sorted(combined_set))
    return result


# print(longest("aretheyhere", "yestheyarehere"))


# 8 kyu Remove duplicates from list
# Define a function that removes duplicates from an array of non-negative numbers and returns it as a result.
# The order of the sequence has to stay the same.
def distinct(seq):
    seen = set()
    result = []
    for num in seq:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))

# 8 kyu Thinkful - Logic Drills: Traffic light
# You're writing code to control your town's traffic lights. You need a
# function to handle each change from green, to yellow, to red, and then to green again. Complete the function that
# takes a string as an argument representing the current state of the light and returns a string representing the
# state the light should change to. For example, when the input is green, output should be yellow.
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'


# print(update_light('green'))

# 7 kyu Find the stray number
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)
def stray(arr):
    unique_num = 0
    for num in arr:
        unique_num ^= num
    return unique_num


# print(stray([1, 1, 1, 1, 1, 1, 2]))


# 7 kyu Largest pair sum in array
# Given a sequence of numbers, find the largest pair sum in the sequence.
# Input sequence contains minimum two elements and every element is an integer.
def largest_pair_sum(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0] + sorted_numbers[1]


# print(largest_pair_sum([10, 14, 2, 23, 19]))

# 8 kyu No Loops 2 - You only need one You will be given an array a and a value x. All you need to do is check
# whether the provided array contains the value, without using a loop. Array can contain numbers or strings. x can be
# either. Return true if the array contains the value, false if not. With strings, you will need to account for case.
def check_a(a, x):
    return x in a

# print(check_a([66, 101], 66))


# 8 kyu 5 without numbers !!
# Write a function that always returns 5
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/
# Good luck :)
def unusual_five():
    return len("abcde")


print(unusual_five())
