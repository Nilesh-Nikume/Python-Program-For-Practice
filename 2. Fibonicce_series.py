n = 6
fib= [0,1]
for i in range(2,n+1):
    new = fib[-1] + fib [-2]
    fib.append(new)
print(fib)

# Using Function
# def Fibonacci_series(Number):
#     fib =[0,1]
#     for i in range(2,Number+1):
#         New_Number = fib[-1] + fib[-2]
#         fib.append(New_Number)
#     print("Fibonacci series is:",fib)
# Number =int(input("Enter the level of fibonacci series: "))
# Fibonacci_series(Number)

# by using generator

# by using generator
# Logic 1
# def fib_generator(n):
#     fib = [0,1]
#     for _ in range(2,n+1):
#         no = fib[-1]+fib[-2]
#         fib.append(no)
#         yield no
# n = int(input("Enter the number"))
# fibonacchi = fib_generator(n)
# for values in fibonacchi:
#     print(values)

# Logic 2
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to generate the first 10 Fibonacci numbers
fibonacci_gen = fibonacci_generator()

for _ in range(10):
    print(next(fibonacci_gen))

