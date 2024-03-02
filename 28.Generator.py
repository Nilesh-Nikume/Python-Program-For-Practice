'''Generator is special type of iterator to allows you to iterate large
values without storing in memories. Generator are use by using keyword yield'''
# pgm 1
# def first_generator():
#     for i in range(5):
#         yield i
# fr = first_generator()
# print(next(fr)) # output 0
# print(next(fr)) # output 1
# print(next(fr)) # output 2

# def first_generator():
#     for i in range(5):
#         yield i
# fr = first_generator()
# for j in fr:
#     print(j)

# fib = [0,1]
# n= 5
# for i in (2,n+1):
#     new = fib[-1] + fib[-2]
#     fib.append(new)
# print(fib)

def generate_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        new = fib[-1] + fib[-2]
        fib.append(new)
        yield new

# Example usage
n = 9
fibonacci_generator = generate_fibonacci(n)

for value in fibonacci_generator:
    print(value)




