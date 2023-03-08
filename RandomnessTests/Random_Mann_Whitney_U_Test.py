from RandomNumber import RandomNumberGenerator

adet= int(input("Üretilecek rastsal sayı adedini giriniz : "))

R, Y, YY = RandomNumberGenerator.RandomNumberGenerator(adet)

# Sort
print(R)
print(Y)
print("....")
for i in range (len(R)):
    for j in range(i,len(R)-1):
        if (R[i]>=R[j]):
            R[i],R[j]=R[j],R[i]
            Y[i],Y[j]=Y[j],Y[i]

print(R)
print(Y)
R_aux =R
Y_aux=[1]
for i in range(len(R)-1):
    if (R[i] == R_aux[i+1]):
        Y_aux.append(Y_aux[i])
    else:
        Y_aux.append(Y_aux[i]+1)

print("---")
print(R)
print(Y_aux)





n1 =0
n2 =0
rn = 0
isaret =[]
TR1, TR2= 0,0
for i in R:
    if (i >=0.5):
        n1 +=1
        isaret.append('+')
    else:
        n2 +=1
        isaret.append('-')
print(isaret)
rn =1
s=isaret[0]
for i in isaret:
    if (i != s):
        rn +=1
    s= i

# Run Test Parameters
print("Test İstatistikleri")


u1 = n1*n2 + n1*(n1+1)/2 - TR1
u2 = n1*n2 + n2*(n2+1)/2 - TR2

u = min (u1,u2)

mu= n1*n2/2
sigma = ((n1*n2*(n1+n2+1))/12)**.5
z=(u-n1*n2/2)/sigma

print ("n1:", n1, ", n2:", n2, ", \u03BC:", mu, ", \u03C3:", sigma, ", z: ",z)
