def reverse(string):
    return string[::-1]


string = "qwerty"
string_2 = reverse(string)
print(string_2)


def palindrome(string):
    string_2 = string[::-1]
    return string_2 == string


string = "olo"
result = palindrome(string)
print(result)
