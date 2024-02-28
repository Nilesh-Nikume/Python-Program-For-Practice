# WAP to find the list of prime numbers between a range of 1 to 100.
# And also find total number of prime numbers.
# a=[]
# for i in range(2,101):
#     for j in range(2,101):
#         if i%j == 0:
#             break
#     if i == j:
#         # print(i,end=",")
#         a.append(i)
# print("Prime Numbers are: ",a)
# print("Total prime numbers in list is: ",len(a))

# -----------------------------------------------------------------------------------------

# Take it input from user
# First_no = int(input("Enter the First-NO where you want to start calculate PRIME no. :"))
# Last_no = int(input("Enter the Last-NO where you want to stop calculate PRIME no. :"))
# Prime_no = []
# print(f"You want to calculate Prime numbers from {First_no} to {Last_no}")
#
# for i in range(First_no+1,Last_no+1):
#     for j in range(First_no+1,Last_no+1):
#         if i % j ==0:
#             break
#     if i == j:
#         Prime_no.append(i)
# print(f"Total Prime between {First_no} to {Last_no}",Prime_no)

First_no = int(input("Enter the First-NO where you want to start calculate PRIME no. :"))
Last_no = int(input("Enter the Last-NO where you want to stop calculate PRIME no. :"))
Prime_no = []

print(f"Are you sure,you want to calculate Prime numbers from {First_no} to {Last_no}")
choice = input("Press 'YES' to calculate or 'NO' to exit: ")

if choice.upper() == 'YES':
    for i in range(First_no+1,Last_no+1):
        for j in range(First_no+1,Last_no+1):
            if i % j ==0:
                break
        if i == j:
            Prime_no.append(i)
    print(f"Prime between {First_no} to {Last_no} is ",Prime_no)
    print(f"Total Prime between {First_no} to {Last_no} is: ", len(Prime_no))

else:
    print("OK Please Enter again")
