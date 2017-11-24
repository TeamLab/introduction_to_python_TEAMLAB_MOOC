from collections import deque
import time

start_time = time.clock()
deque_list = deque()
# Stack
for i in range(10000):
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()
print (time.clock() - start_time, "seconds")

start_time = time.clock()
just_list = []
for i in range(10000):
    for i in range(10000):
        just_list.append(i)
        just_list.pop()
print (time.clock() - start_time, "seconds")

# d.appendleft('f')
# d.popleft()
# d.rotate(1)
# deque(reversed(d))
# d.extendleft('abc')          
