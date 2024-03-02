# def Cloning(li1):
#     li_copy = li1[:] # is used to create a shallow copy of the list.
#     return li_copy
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)
import copy

# by using copy() function
# def Cloning(li1):
#     # li_copy = li1[:] # is used to create a shallow copy of the list.
#     # return li_copy
#     li_copy = li1.copy() # is used to create a shallow copy of the list.
#     return li_copy
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)

# Shallow copy and DeepCopy
# # 1. Need to understand copy concept
# a = [1,2,3,4,5,6] # This line initializes a list a with elements 1, 2, 3, 4, 5, and 6.
# b = a.copy() #This is done to create a separate copy of the list, so changes to one list do not affect the other.
# print("a list before append",a)
# print("b list before append",b)
# b[2]=7
# print("a list after append",a)
# print("b list after append",b)

# 2. Shallow copy
# original_list = [1, [2, 3], 4]
# shallow_copied_list = copy.copy(original_list)
# print(original_list)
# print(shallow_copied_list)
# # Changes in the nested object are reflected in both the original and shallow copy
# shallow_copied_list[1][0] = 'a'
# print(original_list)       # [1, ['a', 3], 4]
# print(shallow_copied_list) # [1, ['a', 3], 4]

#3 Deep Copy

original_list = [1, [2, 3], 4]
deep_copied_list = copy.deepcopy(original_list)

# Changes in the nested object do not affect the original or the deep copy
deep_copied_list[1][0] = 'a'
print(original_list)      # [1, [2, 3], 4]
print(deep_copied_list)   # [1, ['a', 3], 4]



