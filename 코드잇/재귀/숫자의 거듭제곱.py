def power(x, n):
    # 여기에 코드를 작성하세요
    if n == 1:
        return x
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n//2) * power(x, n//2)
    elif n % 2 == 1:
        return x * power(x, n//2) * power(x, n//2)

# 테스트 코드
print(power(2, 3))
print(power(5, 0))
print(power(17, 5))
print(power(3, 17))
print(power(4, 18))
