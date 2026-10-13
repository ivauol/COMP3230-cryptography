# Euclidean Algorithm

def euclid(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(euclid(119, 34))

'''
The Euclidean Algorithm returns the greatest common divisor of two strictly positive integers.
also bc gcd(m, n) == gcd(n, m) we can always just swap them when calculating by hand
'''
