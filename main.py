def capitals(word):
    return [i for i, letter in enumerate(word) if letter.isupper()]


print(capitals("CodEWaRs"))

my_list = ["apple", "banana", "cherry"]

for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")
