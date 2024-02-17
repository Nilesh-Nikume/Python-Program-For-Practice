# WAP to find the list of prime numbers between a range of 1 to 100.
# And also find total number of prime numbers.
a=[]
for i in range(2,101):
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        # print(i,end=",")
        a.append(i)
print("Prime Numbers are: ",a)
print("Total prime numbers in list is: ",len(a))
