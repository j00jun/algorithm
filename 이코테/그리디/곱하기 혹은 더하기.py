n = input()

# answer = 0
# for i in n:
#     if i == '0' or i == '1' or answer==0:
#         answer+=int(i)
#     else:
#         answer*=int(i)

result = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num

print(result)
# print(answer)