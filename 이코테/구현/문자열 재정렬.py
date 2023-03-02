data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
# for i in sorted(word):
#     if ord(i) >= 65:
#         alp.append(i)
#     else:
#         num.appned(i)
