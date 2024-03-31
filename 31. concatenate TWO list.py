# list01 = [12,13,14,15,15,16]
# list02 = [12,13,14,15,15,16,17,18,19]
#
# list03 = list(set(list01 + list02))
# print(list03)

a = [12,3,4,8,7,9]
b = [1,5,7,9,2,3]
c = a + b
print("Before sort",c)
d = list(set(c))
print(f"Dulicate items remove {d}")