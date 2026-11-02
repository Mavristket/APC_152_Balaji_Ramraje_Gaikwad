def count_vowels(s): return sum(1 for c in s if c in "aeiouAEIOU")
def reverse_string(s): return s[::-1]
def is_palindrome(s): return s == s[::-1]
def count_words(s): return len(s.split())
def remove_spaces(s): return s.replace(" ","")
