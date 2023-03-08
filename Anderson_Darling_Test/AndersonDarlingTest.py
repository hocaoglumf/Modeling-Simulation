import math
import random
def AndersonDarlingTest(D):
    D.sort()
    S=0
    N=len(D)
    for j in range(len(D)):
        i = j+1
        S +=(2*i)*(math.log(D[j],math.e) + math.log(1-D[N-1-j],math.e))
    Akare= -N-S/N
    Akare=Akare*(1+.75/N+2.25/N**2)
    return Akare

