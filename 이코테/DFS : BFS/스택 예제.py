stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 마지막에 들어온 7이 나가게 됨
stack.append(1)
stack.append(4)
stack.pop() # 마지막에 들어온 4가 나가게 됨

print(stack)
print(stack[::-1])