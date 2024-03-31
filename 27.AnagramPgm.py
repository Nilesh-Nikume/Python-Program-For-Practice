# def anagramstring(str1,str2):
#     str1 = str1.replace(" ", " ")
#     str2 = str2.replace(" ", " ")
#     return sorted(str1) == sorted(str2)
#
# input1 = input("Enter First string: ")
# input2 = input("Enter Second string: ")
#
# if anagramstring(input1,input2):
#     print(f"Both Strings {input1} and {input2} are Anagram: ")
# else:
#     print(f"Both Strings{input1} and {input2} are NOT Anagram: ")


# Method 2

def check_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print("String are anagram")
    else:
        print("String are not anagram")
s1 = "listen"
s2= "silent"
check_anagram(s1,s2)
