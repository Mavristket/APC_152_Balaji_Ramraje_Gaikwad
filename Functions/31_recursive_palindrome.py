def is_palindrome(text):
    text = str(text).lower()

    def check(left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return check(left + 1, right - 1)

    return check(0, len(text) - 1)


print(is_palindrome("racecar"))
