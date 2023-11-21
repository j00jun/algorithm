# 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

# 떡볶이 떡 만들기(self)
# 이진탐색으로 풀지 못했음 -> 시간초과 위험
n, m = map(int, input().split())

r_h = list(map(int, input().split()))
cut_h = 0

while True:
    new_h = [h - cut_h if h - cut_h > 0 else 0 for h in r_h]
    if sum(new_h) <= m:
        print(cut_h)
        break 
    else:
        cut_h += 1


# 해답 (탐색 범위를 좁혀서)
# 큰 탐색 범위를 보면 먼저 이진 탐색!

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)