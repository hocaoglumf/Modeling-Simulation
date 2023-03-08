from threading import Thread, Lock
import time
import random
N = 0
lock = Lock()
def worker(R):
    global N
    M = N
    N = M + 2**R
    lock.acquire()      # enter safe region
    f = open("D://Temp//paralelx.txt", "a")
    f.write(str(N)+"\n")
    #time.sleep(random.randint(0,5))
    f.close()
    lock.release()      # leave safe region
    return

threads = []
for i in range(15):
    t = Thread(target=worker, args=([i]))
    t.start()
    threads.append(t)

# wait until they finish
for t in threads:
    t.join()

print(f"Value of N is: {N}")