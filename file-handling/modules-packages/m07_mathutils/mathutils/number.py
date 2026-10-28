def is_prime(n): return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
def is_armstrong(n): d = str(n); return n == sum(int(c) ** len(d) for c in d)
def is_palindrome(n): return str(n) == str(n)[::-1]
