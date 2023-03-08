from RandomNumber import RandomNumberGenerator

adet= int(input("Üretilecek rastsal sayı adedini giriniz : "))

R, Y, YY = RandomNumberGenerator.RandomNumberGenerator(adet)

n1 =0
n2 =0
rn = 0
isaret =[]
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
print("Run Test İstatistikleri")
print("# of Run ", rn)
mu= (2*n1*n2)/(n1+n2) +1
sigma = (((2*n1*n2)*(2*n1*n2-n1-n2))/((n1+n2)**2*(n1+n2-1)))**.5
z=(rn-mu)/sigma

print ("n1:", n1, ", n2:", n2, ", \u03BC:", mu, ", \u03C3:", sigma, ", z: ",z)