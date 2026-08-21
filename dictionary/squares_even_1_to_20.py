
even_squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        even_squares[i] = i ** 2


print("Squares of even numbers between 1 and 20:")
print(even_squares)
