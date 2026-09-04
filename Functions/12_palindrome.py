def is_palindrome(value):
    text = str(value).lower()
    return text == text[::-1]


print(is_palindrome("madam"))
