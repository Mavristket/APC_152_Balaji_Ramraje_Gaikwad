from mathutils.basic import *
from mathutils.number import *
from mathutils.statistics import *
a=int(input("Enter first number: ")); b=int(input("Enter second number: "))
nums=list(map(int,input("Enter numbers: ").split())); n=int(input("Enter number to check: "))
print("Add =",add(a,b)); print("Subtract =",subtract(a,b)); print("Multiply =",multiply(a,b)); print("Divide =",divide(a,b))
print("Prime =",prime(n)); print("Armstrong =",armstrong(n)); print("Palindrome =",palindrome(n))
print("Mean =",mean(nums)); print("Maximum =",maximum(nums)); print("Minimum =",minimum(nums))
