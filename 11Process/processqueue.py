#进程间使用队列进行通信
"""
qsize():获取当前队列包含的消息数量
empty():判断队列是否为空
full():判断队列是否为满
get(block=True,timeout):获取队列中的一条消息，然后从队列中移除,空则等待消息
get_nowait():相当于get(block=False)，消息队列为空时，抛出异常
put(item,block=True,timeout):将item消息放入队列,为满则等待
put_nowait(item):相当于put(item,block=False)，空则异常
"""
from multiprocessing import Queue

q=Queue(3)
print("队列是否为空：",q.empty())
print("队列是否为满：",q.full())

q.put('A')
q.put('B')
q.put('C')

print("队列是否为空：",q.empty())
print("队列是否为满：",q.full())

print(q.get())
print(q.get())

print("队列是否为空：",q.empty())
print("队列是否为满：",q.full())
