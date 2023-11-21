import math

# 소수 판별 방법 1
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# 소수 판별 방법 2
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True