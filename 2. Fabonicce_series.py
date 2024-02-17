n = 6
fib= [0,1]
for i in range(2,n+1):
    new = fib[-1] + fib [-2]
    fib.append(new)
print(fib)

# Using Function
def Fibonacci_series(Number):
    fib =[0,1]
    for i in range(2,Number+1):
        New_Number = fib[-1] + fib[-2]
        fib.append(New_Number)
    print("Fibonacci series is:",fib)
Number =int(input("Enter the level of fibonacci series: "))
Fibonacci_series(Number)