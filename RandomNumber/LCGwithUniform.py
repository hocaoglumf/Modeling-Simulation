from RandomNumber import Random_LCG

adet = int(input("Kaç adet rastsal değer üretilecek : "))
alt= float(input("Düzgün dağılım alt değeri : "))
ust= float(input("Düzgün dağılım üst değeri : "))

for i in range(adet):
    drs = alt + Random_LCG.Generate(1)[0] * (ust - alt)
    print(i+1,". ", drs)
