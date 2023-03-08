# Python program to illustrate the concept
# of threading
# importing the threading module
#import threading
from threading import Thread, Lock
import random
import time
import os
lock = Lock()
toplam=1

def Sayac(X,W):
    print(X)
    lock.acquire()
    global toplam
    toplam +=X
    print("Aldım: X=", X, " Bekleme=", W, " Toplam =", toplam, " PID: ", os.getpid())
    time.sleep(W)
    lock.release()



if __name__ == "__main__":

    # creating thread
    prcs=[]
    for i in range(10):
        prcs.append(Thread(target=Sayac, args=(random.randint(1,10),random.randint(10,20))))

    for i in prcs:
        i.start()

    for i in prcs:
        i.join()

    # starting thread 1

    # all threads completely executed
    print("Done!")