def is_prime(n):
    if n < 2: return False
    for i in range(2,n):
        if n%i == 0: return False
    return True
def is_palindrome(n): return str(n) == str(n)[::-1]
def is_armstrong(n):
    s=str(n); return sum(int(x)**len(s) for x in s) == n
def is_perfect(n): return sum(i for i in range(1,n) if n%i==0) == n
