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
    t1 = Thread(target=Sayac, args=(1,10,))
    t2 = Thread(target=Sayac, args=(3,20,))
    t3 = Thread(target=Sayac, args=(10,2,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    t3.start()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    t3.join()


    # all threads completely executed
    print("Done!")