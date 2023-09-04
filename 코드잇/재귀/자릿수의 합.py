def sum_digits(n):
    n = str(n)
    if len(n) <= 1:
        return int(n)
    else:
        return int(n[0]) + sum_digits(n[1:])

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
