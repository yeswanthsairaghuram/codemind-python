def isPrime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def nearestPrime(n):
    if isPrime(n):
        return n
    i = 1
    while True:
        if isPrime(n - i):
            return n - i
        elif isPrime(n + i):
            return n + i
        i += 1
        
t = int(input())
for i in range (t):
    n = int(input())
    res = nearestPrime(n)
    print(res)