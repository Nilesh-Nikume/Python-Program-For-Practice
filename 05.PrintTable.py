# n = 2
# for i in range(1,11):
#     no = n * i
#     print(f"{n} X {i} =", no)
#

def Table(n):
    for i in range(1,11):
        no = n * i
        print(f"{n} X {i} =", no)
n = int(input("Enter Number: "))
Table(n)
