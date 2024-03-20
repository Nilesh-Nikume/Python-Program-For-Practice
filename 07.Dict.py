# WAPeysto put the keys and values of a given dictionary in two different lists.
#------------- Method 1-------------------
# def sep_keys_values(dict):
#     keys_list =list(dict.keys())
#     values_list = list(dict.values())
#     return keys_list,values_list
#
# country_capital_dict = {
#     "Germany": "Berlin",
#     "Italy": "Naples",
#     "England": "London",
#     "Canada": "Ottawa" }
# keys, values = sep_keys_values(country_capital_dict)
# print("Keys in dict is",keys)
# print("values in dict is :", values)

#------------- Method 2-------------------
# country_capital_dict = {
#     "Germany": "Berlin",
#     "Italy": "Naples",
#     "England": "London",
#     "Canada": "Ottawa"}

# print(list(country_capital_dict.keys()))
# print(list(country_capital_dict.values()))

#------------- Method 3-------------------

# def key_value(country_capital_dict):
#     print(list(country_capital_dict.keys()))
#     print(list(country_capital_dict.values()))
# key_value(country_capital_dict)
# country_capital_dict = {
#     "Germany": "Berlin",
#     "Italy": "Naples",
#     "England": "London",
#     "Canada": "Ottawa"}


# WAP to Check if a Given Key Already Exists in Dictionary
# D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}
#
# Key_Name = input("Enter the Key you want to search: ")
#
# def Key_search(Key_Name):
#     if Key_Name in D1:
#         print(f"{Key_Name} is in Dictionary")
#     else:
#         print(f"{Key_Name} is NOT in Dictionary")
# Key_search(Key_Name)

#WAP to find duplicate Values in dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 1}
# #
# # Duplicate= [] # Creating empty list to stored duplicate values
# # seen = set()    # Creating empty set to store all values from dict
# #
# # for item in my_dict.values():
# #     if item in seen:
# #         Duplicate.append(item)
# #     else:
# #         seen.add(item)
# # print(Duplicate)
# #
# my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 1}
#
# def duplicate_values(my_dict):
#     Duplicate_values = []
#     seen = set()
#     for value in my_dict.values():
#         if value in seen:
#             Duplicate_values.append(value)
#         else:
#             seen.add(value)
#     return Duplicate_values
# result = duplicate_values(my_dict)
# print("Duplicate values in Dict are::",result)