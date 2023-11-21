# 기준 데이터 설정 -> 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)로 설정
# 이미 정렬된 배열에서 퀵 정렬 수행 시 매우 느림 

# 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 장점을 살린 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분활된 오른족 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))