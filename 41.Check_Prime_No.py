def is_prime(num):
    if num <= 1:
        return  False
    for item in range(2,int(num**0.5)+1):
        if num % item == 0:
            return False
    return True

def check_prime():
    if is_prime(num):
        print("This is Prime Number")
    else:
        print("This is not Prime Number")
num = int(input("Enter the number: "))
check_prime()