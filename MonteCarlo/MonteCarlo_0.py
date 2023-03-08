import random
'''
0 0.02 0.02 00–02
10 0.30 0.32 03–30
20 0.05 0.37 31–35
30 0.40 0.77 36–75
40 0.15 0.92 76–92
50 0.08 1.00 93–100
'''
MCTable=[[0,0, 2],
         [10, 3,30],
         [20,31,35],
         [30, 36,75],
         [40,76,92],
         [50,93,100]]

N=100000
Repl=50

def FindValue(rnd):
    for i in MCTable:
        if (rnd >= i[1] and rnd <=i[2]):
            return i[0]
    return -1

total=0
rlist=[]
vlist=[]
results=[]
for j in range(Repl):
    total=0
    for i in range(0,N):
        r=random.randint(0,100)
        v=FindValue(r)
        total +=v
    avreg=total/N
    results.append(avreg)

print(results)
mean = sum(results) / len(results)
variance = sum([((x - mean) ** 2) for x in results]) / len(results)
std = variance ** 0.5
print("Ortalama :", round(mean,5), "Standart sapma :", round(std,5))
print("Güven Aralığı : ")
print("  Alt Sınır:",round(mean - 1.96 * std/Repl**.5,5))
print("  Üst Sınır ", round(mean + 1.96 * std/Repl**.5,5))