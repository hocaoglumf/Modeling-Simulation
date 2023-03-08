j = 3
k = 7
mod = 10
jx = input("j :")
j = int(jx)
kx = input("k :")
k = int(kx)
modx = input("Mod :")
mod = int(mod)

numberofrandomX = input("Kaç adet rastsal sayı üretilecek:")
numberofrandom = int(numberofrandomX)

s = [8, 6, 7, 5, 3, 0, 9]
sel = input("Ön tanımlı listeyi kullan (e/h)")

if (sel == "h"):
    ss=[]
    for nn in range(k):
        num = input("List Element ")
        ss.append(int(num))
    s = ss

print("S", s)
random=[]
for n in range(numberofrandom):
    for i in range(len(s)):
        if i is 0:
            out = (s[j-1] * s[k-1]) % mod # the pseudorandom output
        elif 0 < i < k-1:
            s[i] = s[i+1] # shift the array
        else:
            s[i] = out
        random.append(s[i]) # print the result  print("random numbers :",random )
print(random)