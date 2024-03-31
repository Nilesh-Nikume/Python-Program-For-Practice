def My_decorator(fun):
    def wrappar():
        print("I come Before Function call")
        fun()
        print("I come After Function call")
    return wrappar
@My_decorator
def sample_fun():
    print("Hello I am Python ")
sample_fun()
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in number:
    number.append(item * 2)

print(number)




