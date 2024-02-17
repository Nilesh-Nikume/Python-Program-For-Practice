'''Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal)'''

Side_1 = int(input("Enter First side of Triangle: "))

Side_2 = int(input("Enter Second side of Triangle: "))

Side_3 = int(input("Enter Third side of Triangle: "))

if Side_1 == Side_2 and Side_1 == Side_3:
    print("This is  equilateral Triangle means all sides are equal")

elif Side_1 == Side_2 or Side_2 == Side_3 or Side_1 == Side_3:
    print("This is  isosceles Triangle means exactly two sides are equal")
else:
    print("This is  Scalene Triangle means no sides are equal")


