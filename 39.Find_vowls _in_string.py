def vowels_count(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
intpute_string = "Hello, How are you ?"
result =  vowels_count(intpute_string)
print(f"Total Numbers of vowels in this string are {result}")