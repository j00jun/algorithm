n = int(input())

array = []

for i in range(n):
    array.append(list(map(str, input().split())))

array = sorted(array, key= lambda x: int(x[1]))

for j in range(len(array)):
    print(array[j][0], end=' ')

# 해답
n = int(input())

array = []

for i in range(n):
    input_data = input().split()

    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda x: x[1])

for student in array:
    print(student[0], end=' ')