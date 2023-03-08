from RandomValueGeneration import NormalRandomNumber

adet = int(input("Kaç adet rastsal değer üretilecek : "))
ortalama= float(input("Normal dağılım ortalaması : "))
std = float(input("Normal standart sapması : "))

nrsAdet= int(input("Normal rastsal sayı için kullanılacak rastsal sayı adedi : "))
NormalRandomValue=[]
for i in range(adet):
    Nr= NormalRandomNumber.NormalRandomNumber(12)
    c=1
    if (i %2==0):
        c=-1
    Nv=ortalama+c*std*Nr
    NormalRandomValue.append(round(Nv,2))
    print (Nr, "-----> ", round(Nv,2))
print(NormalRandomValue)


