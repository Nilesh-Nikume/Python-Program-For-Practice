def find_duplicatestring(strng):
    duplicate = []
    for item in strng:
        if strng.count(item) > 1:
            if item not in duplicate:
                duplicate.append(item)
    return duplicate


strng = "Selenium"

fd = find_duplicatestring(strng)

print(fd)