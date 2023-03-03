from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 맨 앞에 있는 5 삭제
queue.append(1)
queue.append(4)
queue.popleft() # 맨 앞에 있는 2 삭제

print(queue)
queue.reverse() # 큐 역순
print(queue)