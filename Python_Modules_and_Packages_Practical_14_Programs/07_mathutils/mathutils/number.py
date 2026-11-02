def prime(n):
    if n<2:return False
    for i in range(2,n):
        if n%i==0:return False
    return True
def armstrong(n):
    s=str(n);return sum(int(x)**len(s) for x in s)==n
def palindrome(n): return str(n)==str(n)[::-1]
