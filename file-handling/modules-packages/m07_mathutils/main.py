from mathutils.basic import add, multiply
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum
print("add(4,5) =", add(4, 5), "| multiply(4,5) =", multiply(4, 5))
print("153 prime/armstrong/palindrome:", is_prime(153), is_armstrong(153), is_palindrome(153))
d = [10, 20, 30, 40]
print("mean/max/min:", mean(d), maximum(d), minimum(d))
