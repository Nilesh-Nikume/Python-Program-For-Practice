# General program

str = "Selenium"
duplicate = []
for i in str:
    if str.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)

# Take Input from user

Userstring = input("Enter the string: ")
duplicate_str = []
for i in Userstring:
    if Userstring.count(i) >1:
        if i not in duplicate_str:
            duplicate_str.append(i)
print(duplicate_str)