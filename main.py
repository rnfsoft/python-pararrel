from threading import Thread
from multiprocessing import Process, Queue
from time import time

def work_thread(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

def one_thread(start, end):
    start_time = time()
    result = list()
    th1 = Thread(target=work_thread, args=(1, start, end, result))

    th1.start()
    th1.join()
    print(f"Result with One Thread: {sum(result)}", time()-start_time)

def two_thread(start, end):
    start_time = time()
    result = list()
    th1 = Thread(target=work_thread, args=(1, start, end//2, result))
    th2 = Thread(target=work_thread, args=(2, end//2, end, result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f"Result with Two Threads: {sum(result)}", time()-start_time)

def work_multiprocessing(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

def two_multiprocess(start, end):
    start_time = time()
    result = Queue()

    mp1 = Process(target=work_multiprocessing, args=(1, start, end//2, result))
    mp2 = Process(target=work_multiprocessing, args=(2, end//2, end, result))

    mp1.start()
    mp2.start()
    mp1.join()
    mp2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp

    print(f"Result with Two Multiprocessings: {total}", time()-start_time)
    

if __name__ == "__main__":
    
    START, END  = 0, 100000000
    
    one_thread(START, END)
    two_thread(START, END)
    two_multiprocess(START, END)
    # START, END  = 0, 100
    # Result with One Thread: 4950 0.0009984970092773438
    # Result with Two Threads: 4950 0.0
    # Result with Two Multiprocessings: 4950 0.24685907363891602

    # START, END  = 0, 10000000
    # Result with One Thread: 49999995000000 2.4322712421417236
    # Result with Two Threads: 49999995000000 1.879253625869751
    # Result with Two Multiprocessings: 49999995000000 1.376906156539917

    # START, END  = 0, 100000000
    # Result with One Thread: 4999999950000000 19.144771099090576
    # Result with Two Threads: 4999999950000000 19.0737144947052
    # Result with Two Multiprocessings: 4999999950000000 12.827365159988403
