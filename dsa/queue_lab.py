from myqueue import Queue
import threading
from time import sleep

def place(orders,lock):
    for i in orders:
        lock.acquire()
        q.enqueue(i)
        lock.release()
        print(f'Placed: {i}')
        print('Orders: ',end='')
        q.print()
        print()
        sleep(2)
def serve(lock):
    while q.size():
        try:
            print(f'Served: {q.peek()}')
        except IndexError:
            pass
        lock.acquire()
        q.dequeue()
        lock.release()
        print('Orders: ',end='')
        q.print()
        print()
        sleep(5)

if __name__ == "__main__":
    q = Queue()
    lock = threading.Lock()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target = place,args = (orders,lock))
    t2 = threading.Thread(target = serve,args = (lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()