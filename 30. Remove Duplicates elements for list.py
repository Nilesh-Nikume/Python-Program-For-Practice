#Remove Duplicates from list and arrange them in sorted
list01 = [1,5,4,0,6,9,0,1,3,5,0,0]
#
# new = set(list01) # set is used to remove duplicate
# new = list(set(list01)) # set makes into list
new = sorted(list(set(list01))) # arrange them in sorted manner
print(new)


