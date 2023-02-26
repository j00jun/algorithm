n,m,k = map(int, input().split())

li = list(map(int, input().split()))

li.sort()
first = li[n-1]
second = li[n-2]

count = int(m / (k+1))
count += m % (k + 1)  

result = 0
result += (count) * first
result += (m-count) * second
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m-=1
#     if m == 0:
#         break
#     result += second
#     m -= 1

print(result)
