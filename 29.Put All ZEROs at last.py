# Put all ZEROs at END
#Logic 1
# list01 = [1,5,4,0,6,9,0,1,3,5,0,0]
# for item in list01:
#     if item == 0:
#         list01.remove(item)
#         list01.append(item)
# print(list01)

# Logic 2
# list01 = [1, 5, 4, 0, 6, 9, 0, 1, 3, 5, 0, 0]
#
# # Separate non-zero and zero elements
# non_zeros = [num for num in list01 if num != 0]
# print(non_zeros)
# zeros = [num for num in list01 if num == 0]
# print(zeros)
#
# # Combine non-zero elements and zeros
# result_list = non_zeros + zeros
#
# print(result_list)

list01 = range(1,100)
list01


