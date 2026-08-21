import array

char_array = array.array('u', "Python")
print("Original array:", char_array)

char_array.fromunicode(" Programming")
print("Array after fromunicode():", char_array)
print("Unicode representation:", char_array.tounicode())
