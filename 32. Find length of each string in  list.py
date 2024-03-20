# simple program
#
# list01 = ["Pune","Mumbai","Delhi","Nagpur","Gorkhpur"]
# for city in list01:
#     print(f"Length of {city} is {len(city)}")
#
# list01 = ["Pune", "Mumbai", "Delhi", "Nagpur", "Gorkhpur"]
# for city in list01:
#     print(f"Length of {city} is {len(city)}")

# # get input from user
# Number = int(input("How many cites you want to enter: "))
# city_list = []
# for i in range(Number+1):
#     city = (input(f"Enter the {i+1}: ")).upper()
#     city_list.append(city)
# print(f"List of cities are{city_list}")
# for item in city_list:
#     print(f"Length of {item} is {len(item)}")


def get_len():
    try:
        Number = int(input("How many cites you want to enter: "))
        city_list = []
        for i in range(Number):
            city = (input(f"Enter the {i + 1}: ")).upper()
            city_list.append(city)
        print(f"List of cities are{city_list}")
        for item in city_list:
            print(f"Length of {item} is {len(item)}")
    except  ValueError as V:
        print(V)
get_len()


