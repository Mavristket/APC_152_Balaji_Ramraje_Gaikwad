import array

char_array = array.array('u', "Python")
print("Original array:", char_array)

unicode_string = char_array.tounicode()
print("Converted to unicode string:", unicode_string)
print("Type of output:", type(unicode_string))
