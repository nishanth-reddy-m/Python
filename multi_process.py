import multiprocessing
def process1(n,r,v):
    for index,i in enumerate(n):
        r[index] = i*i
    v.value *= 2
def process2(n,q):
    for i in n:
        q.put(i*i*i)
if __name__ == '__main__':
    n = input('Enter the numbers: ')
    n = list(map(int,n.split()))
    r = multiprocessing.Array('i',len(n))
    v = multiprocessing.Value('d',12.0)
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target = process1,args = (n,r,v))
    p2 = multiprocessing.Process(target=process2, args = (n,q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(list(r),v.value)
    while not q.empty():
        print(q.get())