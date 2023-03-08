def seedLCG(initVal=2342321):
    global rand
    rand = initVal

def lcg():
    #Numerical Recipes
    a = 1664525
    c = 1013904223
    m = 2**24
    global rand
    rand = (a*rand + c) % m
    return rand/m

def Generate(N):
    result = []
    for i in range(N):
        result. append(round(lcg(),3))
    return result

n=int(input("Kaç Adet Rastsal Sayı Üretilecek : "))
sds=input("Bir kök Giriniz : ")
if (len(sds)==0):
    sd=4235354364765513
else:
    sd=int(sds)
seedLCG(sd)
RL=Generate(n)
print(RL)