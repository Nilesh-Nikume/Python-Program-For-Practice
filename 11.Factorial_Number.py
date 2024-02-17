# n = 6
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)
#
def fact(Number):
    Fact_Number = 1
    for i in range(1, Number+1):
        Fact_Number = Fact_Number * i
    print("Factorial is: ", Fact_Number)
Number = int(input("Enter the Number: "))
fact(Number)

# import math
# Number = int(input("Enter the Number: "))
# fact_no = math.factorial(Number)
# print(fact_no)
# # fibo_No = math.fibonaccie(Number)



