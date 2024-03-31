# #without using built-in function
#
# def bubble_sor(arr):
#     n = len(arr)
#     for i in  range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
# list01 = [4,5,6,7,2,9,4,7]
# bubble_sor(list01)
# print(f"Sorted list {list01}")
# print(f"Greatest Number from above list is {list01[-1]}")
#
# # Using built-in function
# list01 = [4,5,6,7,2,9,4,7]
# list01.sort()
# print(f"Sorted list {list01}")
# print(f"Greatest Number from above list is {list01[-1]}")


list01 = [4,5,6,7,2,9,4,7]
max_num = max(x for x in list01)
print(max_num)
