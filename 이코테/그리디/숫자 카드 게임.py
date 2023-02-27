n, m = map(int, input().split())

# result = 0
# for i in range(n):
#     li = list(map(int, input().split()))
#     if min(li) > result:
#         result = min(li)

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)