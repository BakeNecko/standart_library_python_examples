import queue

q = queue.LifoQueue()

if __name__ == '__main__':
    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get(), end=' ')
    print()