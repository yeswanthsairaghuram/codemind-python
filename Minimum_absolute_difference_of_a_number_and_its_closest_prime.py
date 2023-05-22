def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def closest_prime_diff(n):
    if is_prime(n):
        return 0
    else:
        i = n + 1
        while True:
            if is_prime(i):
                break
            i += 1
        j = n - 1
        while True:
            if is_prime(j):
                break
            j -= 1
        return min(abs(n-i), abs(n-j))

n = int(input())
print(closest_prime_diff(n))