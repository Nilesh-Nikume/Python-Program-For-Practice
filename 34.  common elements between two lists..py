def common_in_list():
    list01 = []
    for i in list_a:
        if i in list_b:
            list01.append(i)
    return list01
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = list(map(common_in_list,list_a))
print(result)
