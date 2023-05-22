def isPrime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def megaPrime(n):
    str_n = str(n)
    cnt = 0
    for i in range(len(str_n)):
        if isPrime(int(str_n[i])):
            cnt += 1
    if cnt == len(str_n):
        return True
    return False

n = int(input())
if isPrime(n) and megaPrime(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")