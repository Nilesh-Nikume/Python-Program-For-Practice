# Syntax : newlist = [expression(element) for item in iterable if condition == True]
# Parameter:
#
# expression: Represents the operation you want to execute on every item within the iterable.
# element: The term “variable” refers to each value taken from the iterable.
# iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
# condition: (Optional) A filter helps decide whether or not an element should be added to the new list.
# Advantages of List Comprehension
# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.

# # Program 01 find the square of the number in Python.
# # Method 1 this is gene method
# numbers = [12, 13, 14,15]
# double = []
# for i in numbers:
#     double.append(i**2)
# print("By using general method",double) # output [144, 169, 196]
#
# # Method 2 by using list comprehension
# numbers = [12, 13, 14,15]
# double = [i**2 for i in numbers]
# print("By using list comprehension",double)
#
# #Method 3 printing the list using List Comprehension.
#
# # numbers = [12, 13, 14,15]
# double = [i**2 for i in [12, 13, 14,15]]
# print("printing the list using List Comprehension.",double)
#
# print([i**2 for i in [12, 13, 14,15]])
#
# # Program 02 even numbers from 0 to 10 using List Comprehension
# even_no =[i for i in range(1,11) if i % 2 == 0]
# print(even_no)
#
# number = [[i for i in range(1,5) ]for i in range(3)]
# print(number) # [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


# Program 03 string 'Geeks 4 Geeks!' into a list of its individual characters,
#Metho 01
# string = 'Geeks 4 Geeks'
# list01 = []
# for char in string:
#     list01.append(char)
# print(list01) # ['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's']
#
# string = 'Geeks 4 Geeks'
# list01 = [char for char in string]
# print(list01) # ['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's']

#Cube of numbers exercise question using list comprehension
# cube = [i**3 for i in range(1,11)]
# print(cube)

#  Finding word length exercise question using list comprehension
words = ["apple", "banana", "cherry", "orange"]
# for char in words:
#     print(f"Length of {char} is {len(char)}")
word_length = [len(char) for char in words]
print(f"Length  is {word_length}")