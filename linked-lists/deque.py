from collections import deque

queue = deque()
print(queue)

queue.append('Mary')
queue.append('John')
queue.append('Susan')
print(queue)

queue.popleft()
print(queue)
queue.popleft()
print(queue)