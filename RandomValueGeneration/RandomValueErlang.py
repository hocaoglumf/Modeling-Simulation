from RandomValueGeneration import ExplonentionalRandomNumber

adet= int(input("Kaç adet üretilecek : "))
lmb = float(input("Lambda Değeri :"))
k =int(input ("K değeri : "))

for i in range(adet):
    rv =0
    for j in range(k):
        rv += ExplonentionalRandomNumber.Exp_RND(lmb)
    print(i,". ---->", rv)