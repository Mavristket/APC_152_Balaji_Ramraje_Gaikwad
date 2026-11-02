import recursive_utils as r
n=int(input("Enter a number: "))
print("Factorial =",r.factorial(n))
print("Fibonacci:",end=" ")
for i in range(n): print(r.fibonacci(i),end=" ")
print()
print("Sum of digits =",r.sum_digits(n))
print("Binary =", "0" if n==0 else r.decimal_to_binary(n))
