'''Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year'''

Year = int(input("Enter Year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("This is leap year")
else:
    print("This is not Leap year")