# weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
# cont_dict = {}
# for i in weekdays:
#     if i in cont_dict:
#         cont_dict[i]+=1
#     else:
#         cont_dict[i]=1
# # print(cont_dict) # {'sun': 2, 'mon': 3, 'tue': 1, 'wed': 1, 'thu': 1, 'fri': 1}
# # # Convert the dictionary items to a list of lists
# result = [[key, value] for key,value in cont_dict.items()]
# print(result)   # [['sun', 2], ['mon', 3], ['tue', 1], ['wed', 1], ['thu', 1], ['fri', 1]]

def find_fequnecy(weekdays):
    frequency = {}
    for item in weekdays:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
        list_result = [[key,value] for key,value in frequency.items()]
    return list_result

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
result = find_fequnecy(weekdays)
print(result)
