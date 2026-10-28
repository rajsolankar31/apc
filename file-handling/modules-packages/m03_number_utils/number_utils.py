def is_prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))
def is_palindrome(n): return str(n) == str(n)[::-1]
def is_armstrong(n):
    d = str(n); return n == sum(int(c) ** len(d) for c in d)
def is_perfect(n): return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n
